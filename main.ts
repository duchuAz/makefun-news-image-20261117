import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

// A deliberately small entry program: validate the checked-in image, then
// publish exactly those bytes into the scoring directory.
type CheckedImage = {
  readonly bytes: Buffer;
  readonly width: number;
  readonly height: number;
};

const PNG_SIGNATURE = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
const MAX_IMAGE_BYTES = 1024 * 1024;
const MAX_EDGE = 1024;

function fail(message: string): never {
  process.stderr.write(`entry: ${message}\n`);
  process.exit(1);
}

function readUInt32(bytes: Buffer, offset: number): number {
  if (offset + 4 > bytes.length) fail("PNG header is truncated");
  return bytes.readUInt32BE(offset);
}

function inspectPng(bytes: Buffer): CheckedImage {
  if (bytes.length === 0) fail("entry.png is empty");
  if (bytes.length > MAX_IMAGE_BYTES) fail(`entry.png is ${bytes.length} bytes; the limit is ${MAX_IMAGE_BYTES}`);
  if (!bytes.subarray(0, PNG_SIGNATURE.length).equals(PNG_SIGNATURE)) fail("entry.png is not a PNG");
  if (bytes.length < 33) fail("entry.png has no complete IHDR chunk");
  const chunkType = bytes.subarray(12, 16).toString("ascii");
  if (chunkType !== "IHDR") fail("the first PNG chunk is not IHDR");
  const width = readUInt32(bytes, 16);
  const height = readUInt32(bytes, 20);
  if (width < 1 || height < 1 || width > MAX_EDGE || height > MAX_EDGE) {
    fail(`entry.png is ${width}x${height}; each edge must be at most ${MAX_EDGE}`);
  }
  return { bytes, width, height };
}

function loadEntry(): CheckedImage {
  const source = join(process.cwd(), "entry.png");
  let bytes: Buffer;
  try {
    bytes = readFileSync(source);
  } catch (error) {
    fail(`cannot read ${source}: ${error instanceof Error ? error.message : String(error)}`);
  }
  return inspectPng(bytes);
}

function outputDirectory(): string {
  const configured = process.env.MAKEFUN_OUTPUT_DIR;
  if (configured && configured.length > 0) return configured;
  return "/output";
}

function main(): void {
  const image = loadEntry();
  const destination = outputDirectory();
  try {
    mkdirSync(destination, { recursive: true });
    writeFileSync(join(destination, "entry.png"), image.bytes);
  } catch (error) {
    fail(`cannot write the image: ${error instanceof Error ? error.message : String(error)}`);
  }
  process.stdout.write(`wrote ${image.width}x${image.height} PNG, ${image.bytes.length} bytes\n`);
}

main();
