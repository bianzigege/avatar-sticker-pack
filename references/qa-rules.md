# Sticker QA Rules

Reject an image or pack when any required check fails.

## Per-image checks

- Square output with an actual alpha channel.
- No baked checkerboard, opaque white background, watermark, or accidental text.
- The character matches the supplied avatar's stable identity features.
- The chosen track is correct: natural proportions for `real`, consistent 2.5–3 heads for `q`.
- Signature hairstyle, accessory, clothing cue, or color remains visible.
- One clear intent; the action reads at thumbnail size.
- Hands, face, main prop, and signature feature are not clipped.
- Text is exact, legible, and placed inside the safe area.
- White outline is consistent and does not erase fine details.

## Pack-level checks

- All images in the same track share line/rendering language, palette, outline, and typography.
- Paired `real` and `q` images communicate the same intent.
- The two tracks differ intentionally in proportion and expression strength.
- No pose, crop, or prop is repeated without a reason.
- Filenames map unambiguously to the exact text or intent.
- Original generated files remain separate from final exports.

## Fast rejection questions

1. Would the user recognize the avatar without reading the text?
2. Does the expression communicate the intent in one second?
3. Is this clearly the requested track?
4. Does the file remain usable on a dark or light chat background?
