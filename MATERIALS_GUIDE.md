# 素材放置说明

现在按“内容对象”管理素材，而不是只按图片、音频、视频分类。

核心规则：

- `assets/`：准备公开、网站会引用的素材。
- `materials/`：原始素材和临时素材，默认不发布。
- `_works/`：项目/论文的文字。
- `_posts/`：正式发布的博客文章。
- `_drafts/`：还没发布的草稿。

## 全站共用素材

放在：

- `assets/shared/portraits/`：头像、About 页照片。
- `assets/shared/gallery/`：首页生活/实验室/gallery 图片。
- `assets/shared/icons/`：favicon、站点小图标。

原始照片如果还没决定用途，先放：

- `materials/inbox/photos/`

## 项目素材

每个项目有自己的文件夹：

- `assets/works/eva/`
- `assets/works/phaseflow/`
- `assets/works/proteocraft/`
- `assets/works/rl-diffusion/`
- `assets/works/alphaenzyme/`
- `assets/works/syntharchitect/`

每个项目的推荐文件名：

- `cover.png`：项目封面。
- `figure-1.png`：正文图。
- `architecture.png`：模型结构图。
- `demo.mp4`：短 demo 视频。
- `audio-note.mp3`：短音频说明。

对应的原始素材放：

- `materials/works/<project>/raw-images/`
- `materials/works/<project>/raw-videos/`
- `materials/works/<project>/notes/`

项目文字改：

- `_works/<project>.md`

## 博客素材

正式博客文章放：

- `_posts/`

文件名格式：

- `2026-07-05-my-first-note.md`

每篇博客自己的图片、音频、视频放：

- `assets/posts/<post-slug>/`

例如：

- `assets/posts/2026-07-05-my-first-note/hero.jpg`
- `assets/posts/2026-07-05-my-first-note/audio-note.mp3`
- `assets/posts/2026-07-05-my-first-note/clip.mp4`

博客原始素材放：

- `materials/posts/<post-slug>/`

## Cat / Pixie

Pixie 页面的公开素材放：

- `assets/cat/pixie/`

例如：

- `cover.png`
- `photo-01.jpg`
- `meow-01.m4a`
- `clip-01.mp4`

Pixie 的原始照片、视频、随手笔记放：

- `materials/cat/pixie/raw-photos/`
- `materials/cat/pixie/raw-video/`
- `materials/cat/pixie/notes/`

中文名如果要保密，不要写进 `assets/` 或公开页面里。

## Life / 临时收纳

生活类但还没决定要不要变成博客的材料放：

- `materials/life/`

所有临时材料先丢这里也可以：

- `materials/inbox/photos/`
- `materials/inbox/text/`
- `materials/inbox/audio/`
- `materials/inbox/video/`
- `materials/inbox/documents/`

## 公开文档

准备公开下载的文件放：

- `assets/files/cv/`：公开版 CV PDF。
- `assets/files/posters/`：论文 poster。
- `assets/files/slides/`：报告 slides。

还没准备公开的文档放：

- `materials/inbox/documents/`

不要把手机号、未公开论文、保密合作文件、私人证件等放进 `assets/`，因为 `assets/` 默认会随网站发布。
