#!/usr/bin/env node
/**
 * postinstall: Copy .github/ skills to the consuming project's .github/
 *
 * Merges (not overwrites) into the target .github/ directory so existing
 * files like workflows are preserved.
 */

const fs = require("fs");
const path = require("path");

const src = path.join(__dirname, ".github");
const projectRoot = findProjectRoot(__dirname);
if (!projectRoot) {
  console.log("[spread1000-researcher] Could not find project root. Skipping postinstall.");
  process.exit(0);
}

const dest = path.join(projectRoot, ".github");

// Only run when installed as a dependency (not standalone)
if (path.resolve(__dirname) === path.resolve(projectRoot)) {
  process.exit(0);
}

copyDirRecursive(src, dest);
console.log("[spread1000-researcher] Skills deployed to .github/");

function findProjectRoot(startDir) {
  // Walk up from node_modules/@nahisaho/spread1000-researcher to find the
  // consuming project's package.json
  let dir = startDir;
  for (let i = 0; i < 10; i++) {
    const parent = path.dirname(dir);
    if (parent === dir) return null;
    dir = parent;
    // Stop at the first package.json outside node_modules
    const hasPkg = fs.existsSync(path.join(dir, "package.json"));
    const inNodeModules = dir.split(path.sep).includes("node_modules");
    if (hasPkg && !inNodeModules) {
      return dir;
    }
  }
  return null;
}

function copyDirRecursive(srcDir, destDir) {
  if (!fs.existsSync(srcDir)) return;
  fs.mkdirSync(destDir, { recursive: true });

  for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
    const srcPath = path.join(srcDir, entry.name);
    const destPath = path.join(destDir, entry.name);

    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}
