# Customization

Support natural language first. A user may provide only an avatar and a sentence, or may control any of the fields below.

## Supported controls

| field | examples | rule |
|---|---|---|
| `preset` | `compact`, `standard`, `full` | 6, 12, or 24 paired intents |
| `tracks` | `real`, `q`, `both` | Generate only the requested track(s) |
| `intents` | `收到、搞定、请补充信息` | Treat supplied copy as exact text |
| `tone` | 专业、亲切、搞笑、克制、热血 | Change expression and action, not identity |
| `palette` | 黑白+橙蓝、品牌色、低饱和 | Keep palette consistent across the selected track |
| `props` | 电脑、放大镜、茶杯、任务清单 | Use one main prop per sticker unless requested otherwise |
| `proportion` | 成人比例、2.5头身、3头身 | Apply independently to each track |
| `text_style` | 黑体、手写、圆润、无文字 | Keep exact copy; only style and placement may vary |
| `output_size` | 512、1024、2048 | Export square master PNGs at the requested size |
| `platform` | 微信、飞书、Slack、Discord | Follow the platform constraints when specified |

## Natural-language examples

```text
只做 Q 版，生成 12 个工作场景表情，语气专业但有一点幽默，文案用：
收到、马上处理、稍等一下、请补充信息、需要确认、进度同步、稳了、搞定、
再检查一下、已交付、可验收、收工。
```

```text
真人版和 Q 版都要。沿用头像的黑白线稿，保留橙蓝点缀；自定义文案：
早上好、今天也要加油、我先看一下、这个可以、让我缓缓、辛苦了。
每张 1024×1024，透明背景，文字后加。
```

If the user gives fewer custom labels than the requested count, do not silently invent more labels. Ask whether to repeat, use the intent library, or reduce the count.
