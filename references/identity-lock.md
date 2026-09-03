# Identity Lock

Use this reference to convert an avatar image into a short, stable identity specification.

## What to lock

Lock only features that are visible and distinctive in the supplied reference:

- head and face silhouette;
- hair silhouette, part, length, and color;
- eyebrow and eye shape;
- facial marks, glasses, facial hair, or other stable details;
- clothing silhouette and one or two signature garments;
- distinctive accessory, prop, or color;
- rendering language: photo, ink, vector, painted, 3D, or mixed.

## What may vary

- expression;
- pose and gesture;
- body orientation;
- small contextual props;
- motion marks and emotion symbols;
- text and text placement.

## What to forbid

Create generic prohibitions from the input rather than copying another person's rules:

- no second human character;
- no changed hairstyle or signature accessory;
- no unrelated costume or palette;
- no watermark or accidental brand mark;
- no extra text when text is being added after generation;
- no photorealism when the source is illustrated;
- no chibi proportions in `real` mode;
- no adult-proportion drift in `q` mode.

## Identity lock template

```text
IDENTITY LOCK — highest priority
Use the supplied avatar as the only identity reference.
Keep: [face/head], [hair], [eyes/brows], [clothing], [signature accessory], [palette], [rendering language].
Change only: expression, pose, gesture, contextual prop, and sticker text.
Do not create a second person, new hairstyle, new signature accessory, unrelated costume, watermark, or accidental text.
```

Do not store the original avatar in the skill repository. Write this lock for the current task only.
