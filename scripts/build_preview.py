from __future__ import annotations

import html
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"

SITE_TITLE = "Yanjie Huang"
SITE_DESC = "AI4Bio, photos, projects, and small field notes."
EMAIL = "huangyanjie@sjtu.edu.cn"
GITHUB = "https://github.com/kevinhyj"
AUTHOR_IMAGE = "/assets/shared/portraits/home-window.jpeg"
HERO_IMAGE = "/assets/shared/portraits/home-window.jpeg"
AUTHOR_BIO = "AI4Bio, foundation models, snow, notes, and Pixie someday."
GALLERY = [
    ("/assets/posts/2026-04-23-keketuohai-skiing/07-tanboer-slope.jpg", "Keketuohai snowboarding blog cover"),
    ("/assets/posts/2025-02-21-hokkaido-junk/00-otaru-snow-night.jpg", "Hokkaido blog cover"),
    ("/assets/posts/2024-10-30-nara-deer/06-ema-wishes.jpg", "Nara blog cover"),
    ("/assets/posts/2024-10-26-osaka-universal-yoasobi/00-yoasobi-main-stage.jpg", "Osaka blog cover"),
]


def parse_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    _, raw, body = text.split("---", 2)
    data: dict[str, object] = {}
    current_list = None
    current_item = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list:
            value = line[4:].strip()
            if ":" in value:
                key, val = value.split(":", 1)
                current_item = {key.strip(): clean_yaml_value(val)}
                data[current_list].append(current_item)
            else:
                data[current_list].append(clean_yaml_value(value))
                current_item = None
        elif line.startswith("    ") and current_item is not None:
            key, val = line.strip().split(":", 1)
            current_item[key.strip()] = clean_yaml_value(val)
        elif line.endswith(":"):
            current_list = line[:-1].strip()
            data[current_list] = []
            current_item = None
        elif ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = clean_yaml_value(val)
            current_list = None
            current_item = None
    return data, body.strip()


def clean_yaml_value(value: str):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value


def inline(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def markdown_to_html(markdown: str) -> str:
    blocks = []
    lines = [line.rstrip() for line in markdown.strip().splitlines()]
    paragraph = []
    in_list = False
    for line in lines:
        if not line:
            if paragraph:
                blocks.append("<p>" + inline(" ".join(paragraph)) + "</p>")
                paragraph = []
            if in_list:
                blocks.append("</ul>")
                in_list = False
            continue
        if line.startswith("## "):
            if paragraph:
                blocks.append("<p>" + inline(" ".join(paragraph)) + "</p>")
                paragraph = []
            if in_list:
                blocks.append("</ul>")
                in_list = False
            blocks.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.lstrip().startswith("<"):
            if paragraph:
                blocks.append("<p>" + inline(" ".join(paragraph)) + "</p>")
                paragraph = []
            if in_list:
                blocks.append("</ul>")
                in_list = False
            blocks.append(line)
        elif line.startswith("- "):
            if paragraph:
                blocks.append("<p>" + inline(" ".join(paragraph)) + "</p>")
                paragraph = []
            if not in_list:
                blocks.append("<ul>")
                in_list = True
            blocks.append(f"<li>{inline(line[2:])}</li>")
        else:
            paragraph.append(line)
    if paragraph:
        blocks.append("<p>" + inline(" ".join(paragraph)) + "</p>")
    if in_list:
        blocks.append("</ul>")
    return "\n".join(blocks)


def render_liquid_paths(text: str) -> str:
    text = re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", r"\1", text)
    text = re.sub(r'\{\{\s*"([^"]+)"\s*\|\s*relative_url\s*\}\}', r"\1", text)
    return text


def parse_date(value: str):
    raw = str(value).strip()
    for pattern in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S %z"):
        try:
            return datetime.strptime(raw, pattern)
        except ValueError:
            continue
    return None


def display_date(value: str) -> str:
    parsed = parse_date(value)
    return parsed.strftime("%d %b %Y") if parsed else str(value)


def long_display_date(value: str) -> str:
    parsed = parse_date(value)
    return parsed.strftime("%B %-d, %Y") if parsed else str(value)


def datetime_value(value: str) -> str:
    parsed = parse_date(value)
    return parsed.isoformat() if parsed else str(value)


def default_layout(title: str, body: str, description: str = "") -> str:
    page_title = SITE_TITLE if title == "Home" else f"{html.escape(title)} | {SITE_TITLE}"
    desc = html.escape(description or SITE_DESC)
    gallery = "\n".join(f'<img src="{src}" alt="{html.escape(alt)}">' for src, alt in GALLERY)
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{page_title}</title>
    <meta name="description" content="{desc}">
    <link rel="icon" href="/assets/shared/icons/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="/assets/css/styles.css">
  </head>
  <body>
    <header class="site-header">
      <div class="container">
        <a class="site-logo" href="/" aria-label="Yanjie Huang home">Yanjie Huang</a>
        <nav class="site-nav" aria-label="Main navigation">
          <a href="/">Home</a>
          <a href="/projects/">Projects</a>
          <a href="/cv/">CV</a>
          <a href="/blog/">Blog</a>
          <div class="nav-dropdown">
            <button class="nav-trigger" type="button" aria-haspopup="true">Pages</button>
            <div class="nav-submenu">
              <a href="/cat/">Cat</a>
              <a href="/contact/">Contact</a>
            </div>
          </div>
        </nav>
      </div>
    </header>
    <main class="content" aria-label="Content">{body}</main>
    <section class="footer-gallery" aria-label="Photo gallery">{gallery}</section>
    <footer class="site-footer">
      <div class="container footer-grid">
        <div class="footer-author">
          <img src="{AUTHOR_IMAGE}" alt="Yanjie Huang">
          <div>
            <h3>Yanjie Huang</h3>
            <p>{AUTHOR_BIO}</p>
          </div>
        </div>
        <div class="footer-links">
          <a href="mailto:{EMAIL}">Email</a>
          <a href="{GITHUB}">GitHub</a>
          <a href="/cat/">Pixie</a>
        </div>
        <nav class="footer-nav" aria-label="Footer navigation">
          <a href="/">Home</a>
          <a href="/projects/">Projects</a>
          <a href="/cv/">CV</a>
          <a href="/blog/">Blog</a>
          <a href="/cat/">Cat</a>
          <a href="/contact/">Contact</a>
        </nav>
      </div>
    </footer>
  </body>
</html>
"""


def page_head(title: str, eyebrow: str, subtitle: str) -> str:
    return f"""<section class="page-head">
  <div class="container">
    <p class="eyebrow">{html.escape(eyebrow)}</p>
    <h1>{html.escape(title)}</h1>
    <p>{html.escape(subtitle)}</p>
  </div>
</section>"""


def load_works():
    works = []
    for path in (ROOT / "_works").glob("*.md"):
        data, body = parse_front_matter(path)
        data["slug"] = path.stem
        data["url"] = f"/work/{path.stem}/"
        data["body"] = body
        if str(data.get("hidden", "")).lower() != "true":
            works.append(data)
    return sorted(works, key=lambda item: int(item.get("order", 999)))


def load_posts():
    posts = []
    for path in (ROOT / "_posts").glob("*.md"):
        if path.name.startswith("."):
            continue
        data, body = parse_front_matter(path)
        slug = path.stem[11:] if re.match(r"\d{4}-\d{2}-\d{2}-", path.stem) else path.stem
        data["slug"] = slug
        data["url"] = f"/blog/{slug}/"
        data["body"] = body
        posts.append(data)
    return sorted(posts, key=lambda item: str(item.get("date", "")), reverse=True)


def project_card(work, heading="h3") -> str:
    status = '<span class="project-status">In progress</span>' if work.get("status") == "In progress" else ""
    image = f'<img src="{work["image"]}" alt="{html.escape(work["title"])} visual">' if work.get("image") else f'<div class="project-placeholder" role="img" aria-label="{html.escape(work["title"])} image coming soon">?</div>'
    return f"""<a class="project-card project-card-{work['slug']}" href="{work['url']}">
  {image}
  <div class="card-content">
    <p>{html.escape(work.get('kind', 'Project'))}{status}</p>
    <{heading}>{html.escape(work['title'])}</{heading}>
    <span>{html.escape(work.get('subtitle', ''))}</span>
  </div>
</a>"""


def post_card(post) -> str:
    tags = " / ".join(post.get("tags", []))
    return f"""<a class="post-card" href="{post['url']}">
  <img src="{post.get('image', '/assets/shared/gallery/gallery-life.png')}" alt="{html.escape(post['title'])} cover">
  <div>
    <p class="post-card-tags">{html.escape(tags)}</p>
    <h3>{html.escape(post['title'])}</h3>
    <p>{html.escape(post.get('excerpt', ''))}</p>
  </div>
</a>"""


def write_page(path: str, title: str, body: str, description: str = ""):
    if path == "/":
        target = OUT / "index.html"
    elif path.endswith(".html"):
        target = OUT / path.strip("/")
    else:
        target = OUT / path.strip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(default_layout(title, body, description), encoding="utf-8")


def build_home(works, posts):
    project_cards = "\n".join(project_card(work) for work in works[:6])
    post_cards = "\n".join(post_card(post) for post in posts[:3])
    body = f"""<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-image">
        <img src="{HERO_IMAGE}" alt="Yanjie Huang by a winter window">
      </div>
      <div class="hero-copy">
        <h1>I'm Yanjie. What do I do for a living? I dream.</h1>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <h2>Latest works</h2>
        <p>AI4Bio projects, generative models, and scientific agents.</p>
      </div>
      <a href="/projects/">See all</a>
    </div>
    <div class="project-grid">{project_cards}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <div><h2>Recent Posts</h2></div>
      <a href="/blog/">See all</a>
    </div>
    <div class="post-card-grid">{post_cards}</div>
  </div>
</section>"""
    write_page("/", "Home", body)


def build_works(works):
    cards = "\n".join(project_card(work, "h3") for work in works)
    body = page_head("Projects", "Projects", "AI4Bio systems, generative models, and scientific agents.")
    body += f"""<section class="section page-section">
  <div class="container">
    <div class="project-grid all-projects">{cards}</div>
  </div>
</section>"""
    write_page("/projects/", "Projects", body)

    for work in works:
        links = ""
        if work.get("links"):
            links += "<h2>Links</h2>"
            for link in work["links"]:
                url = html.escape(link["url"])
                target = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
                links += f'<a href="{url}"{target}>{html.escape(link["label"])}</a>'
        tags = ""
        if work.get("tags"):
            tags = "<h2>Tags</h2><div class=\"tag-list\">" + "".join(f"<span>{html.escape(tag)}</span>" for tag in work["tags"]) + "</div>"
        meta = "".join(
            f"<span>{html.escape(str(value))}</span>"
            for value in (work.get("year"), work.get("role"), work.get("status"))
            if value
        )
        body = f"""<article class="project-page">
  <div class="container">
    <a class="back-link" href="/projects/">Back to projects</a>
    <header class="project-head">
      <div>
        <p class="eyebrow">{html.escape(work.get('kind', 'Project'))}</p>
        <h1>{html.escape(work['title'])}</h1>
        <p>{html.escape(work.get('subtitle', ''))}</p>
        <div class="meta-row">{meta}</div>
      </div>
      {f'<img src="{work.get("detail_image", work["image"])}" alt="{html.escape(work["title"])} visual">' if work.get("detail_image", work.get("image")) else f'<div class="project-placeholder project-placeholder-detail" role="img" aria-label="{html.escape(work["title"])} image coming soon">?</div>'}
    </header>
    <div class="project-content">
      <div class="prose">{markdown_to_html(work['body'])}</div>
      <aside class="side-panel">{links}{tags}</aside>
    </div>
  </div>
</article>"""
        write_page(work["url"], work["title"], body)


def build_blog(posts):
    body = page_head("Blog", "Blog", "Photo notes, research fragments, and a little everyday life.")
    if posts:
        body += '<section class="section page-section"><div class="container"><div class="post-card-grid blog-grid">'
        body += "\n".join(post_card(post) for post in posts)
        body += "</div></div></section>"
    else:
        body += '<section class="section page-section"><div class="container"><div class="empty-state"><h2>The notebook is open, but the ink is still drying.</h2><p>Research logs, paper notes, and life fragments will live here.</p></div></div></section>'
    write_page("/blog/", "Blog", body)


def build_posts(posts):
    for post in posts:
        tags = "".join(f'<a href="/blog/">{html.escape(tag)}</a>' for tag in post.get("tags", []))
        is_instagram = "instagram" in post.get("tags", [])
        orbit = ""
        if is_instagram:
            orbit = f"""<div class="instagram-orbit-notes" aria-hidden="true">
        <span>@kevinhyj</span>
                <span>{html.escape(long_display_date(post.get('date', '')))}</span>
        <span>drag the space</span>
      </div>"""
        body = f"""<header class="post-head{' instagram-post-head' if is_instagram else ''}">
  <div class="container">
    <div class="post-tags">{tags}</div>
    <h1>{html.escape(post['title'])}</h1>
    <p class="post-meta"><a href="/cv/">Yanjie Huang</a><span>–</span><time datetime="{html.escape(datetime_value(post.get('date', '')))}">{display_date(post.get('date', ''))}</time></p>
    {orbit}
  </div>
</header>
<article class="post{' instagram-post' if is_instagram else ''}">
  <div class="container">"""
        if is_instagram:
            body += '<div class="instagram-sound-panel"><span class="instagram-source-link">Photo archive</span></div>'
        elif post.get("image"):
            body += f'<img class="post-image" src="{post["image"]}" alt="{html.escape(post["title"])}">'
        body += f'<div class="post-content">{render_liquid_paths(post["body"])}</div>'
        if post.get("gallery"):
            body += '<div class="instagram-grid">'
            for image in post["gallery"]:
                klass = html.escape(image.get("class", ""))
                body += f'<img class="{klass}" src="{image["src"]}" alt="{html.escape(image["alt"])}">'
            body += "</div>"
        body += "</div></article>"
        write_page(post["url"], post["title"], body, post.get("excerpt", ""))


def build_simple_page(source: str):
    data, body = parse_front_matter(ROOT / source)
    body = render_liquid_paths(body)
    if not data.get("hide_title"):
        body = page_head(data["title"], data.get("eyebrow", "Pages"), data.get("subtitle", "")) + body
    write_page(data["permalink"], data["title"], body)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    works = load_works()
    posts = load_posts()
    build_home(works, posts)
    build_works(works)
    build_blog(posts)
    build_posts(posts)
    build_simple_page("cv.md")
    build_simple_page("cat.md")
    build_simple_page("contact.md")
    write_page("/works/", "Projects", '<section class="section page-section"><div class="container"><div class="empty-state"><h2>Works moved to Projects.</h2><p>The research portfolio now lives at <a href="/projects/">Projects</a>.</p><a class="button" href="/projects/">Open Projects</a></div></div></section>')
    write_page("/404.html", "Page Not Found", '<section class="section page-section"><div class="container"><div class="empty-state"><h2>This path has not grown a page yet.</h2><p>Try the home page, projects, blog, CV, contact, or Pixie page.</p><a class="button" href="/">Return home</a></div></div></section>')
    (OUT / "robots.txt").write_text((ROOT / "robots.txt").read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Built preview at {OUT}")


if __name__ == "__main__":
    main()
