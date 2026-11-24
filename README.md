# pairwise-indirect-draw-compaction

## 领域

游戏、图形与多媒体

## 主题

间接绘制计数压缩回读

## 说明

帧号配对、追加栅栏与确定性排序键。

初始状态下 `graphics/indirect_draw_compaction.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
