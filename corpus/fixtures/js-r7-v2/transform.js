const alphabet = 'abcdefghijklmnopqrstuvwxyz';
function rot13(input) {
  return String(input).replace(/[a-z]/g, c => alphabet[(alphabet.indexOf(c) + 13) % 26]);
}
function checksum(input) {
  let state = 0x13579bdf;
  for (const c of input) {
    state = ((state << 5) | (state >>> 27)) ^ (c.charCodeAt(0) + 17);
  }
  return state >>> 0;
}
module.exports = { rot13, checksum };
