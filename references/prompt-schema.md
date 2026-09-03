# Prompt Schema

Assemble one prompt per image using the sections below. Keep the shared identity and mode text fixed across the track; vary only the intent fields.

```text
Use case: illustration-story
Asset type: standalone square transparent chat sticker
Input images: Image 1 is the user's avatar identity reference; Image 2 is an optional approved style anchor for this track

Primary request:
Generate one independent sticker for the intent "[EXACT TEXT]".

Identity lock:
[task-specific identity lock from identity-lock.md]

Mode lock:
[real-mode.md or q-mode.md]

Action:
[one clear action that communicates the intent]

Composition:
Square canvas, one character, centered readable silhouette, all important features inside safe margins, transparent background, restrained white die-cut outline, limited orange/yellow/blue accents only when they support the action.

Text:
Do not generate text inside the image. The exact text will be added after generation.

Avoid:
extra people, changed identity, changed hairstyle, changed signature accessory, unrelated clothing, fake checkerboard background, watermark, logo, dense background, formal infographic, poster layout, accidental letters, and cropped hands or signature features.
```

For a user who explicitly requests text inside the generated image, quote the text verbatim and ask the model to render it once; still verify every character afterward.
