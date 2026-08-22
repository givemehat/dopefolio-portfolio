import os
import re

html_files = ["index.html", "project-1.html", "project-2.html", "project-3.html"]

def update_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title and Meta Description, add OG tags
    content = re.sub(
        r'<title>.*?</title>',
        '<title>Rajnish Singh | AI & ML Researcher</title>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    og_tags = """    <meta name="description" content="Rajnish Singh — AI/ML Researcher, Quantum Computing Advocate, and Software Engineer. B.Tech CSE, IBM Qiskit Advocate, McKinsey Forward Program alum." />
    <meta property="og:title" content="Rajnish Singh | AI & ML Researcher" />
    <meta property="og:description" content="Rajnish Singh — AI/ML Researcher, Quantum Computing Advocate, and Software Engineer. B.Tech CSE, IBM Qiskit Advocate, McKinsey Forward Program alum." />
    <meta property="og:image" content="./assets/jpeg/profile.jpeg" />
    <meta property="og:url" content="https://givemehat.github.io/dopefolio-portfolio/" />
    <meta property="og:type" content="website" />"""
    
    content = re.sub(
        r'<meta name="description" content=".*?"\s*/>',
        og_tags,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 2. Update Navigation (Header)
    nav_addition = """            <li class="header__link-wrapper">
              <a href="./index.html#projects" class="header__link"> Projects </a>
            </li>
            <li class="header__link-wrapper">
              <a href="./index.html#certifications" class="header__link"> Certifications </a>
            </li>
            <li class="header__link-wrapper">
              <a href="./index.html#publications" class="header__link"> Publications </a>
            </li>
            <li class="header__link-wrapper">
              <a href="./assets/pdf/resume.pdf" class="header__link" target="_blank"> Resume </a>
            </li>"""
    content = re.sub(
        r'<li class="header__link-wrapper">\s*<a href="\./index\.html#projects" class="header__link">\s*Projects\s*</a>\s*</li>',
        nav_addition,
        content
    )

    # 3. Social Links (Hero & Footer) - We will just replace the entire social blocks
    # Hero social links
    hero_socials = """          <a href="https://linkedin.com/in/rajnish-singh-a9a61022a" class="home-hero__social-icon-link" target="_blank">
            <img src="./assets/png/linkedin-ico.png" alt="LinkedIn" class="home-hero__social-icon" />
          </a>
          <a href="https://github.com/givemehat" class="home-hero__social-icon-link" target="_blank">
            <img src="./assets/png/github-ico.png" alt="GitHub" class="home-hero__social-icon" />
          </a>
          <a href="https://medium.com/@rajnishsingh" class="home-hero__social-icon-link" target="_blank">
            <img src="./assets/png/medium-ico.png" alt="Medium" class="home-hero__social-icon" style="filter: invert(1); width:32px; height:32px;" />
          </a>"""
    content = re.sub(
        r'<div class="home-hero__socials">.*?</div>',
        f'<div class="home-hero__socials">\n{hero_socials}\n        </div>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Footer social links
    footer_socials = """              <a href="https://linkedin.com/in/rajnish-singh-a9a61022a" target="_blank" class="home-hero__social-icon-link">
                <img src="./assets/png/linkedin-ico.png" alt="LinkedIn" />
              </a>
              <a href="https://github.com/givemehat" target="_blank" class="home-hero__social-icon-link">
                <img src="./assets/png/github-ico.png" alt="GitHub" />
              </a>
              <a href="https://medium.com/@rajnishsingh" target="_blank" class="home-hero__social-icon-link">
                <img src="./assets/png/medium-ico.png" alt="Medium" style="filter: invert(1); width:24px; height:24px;" />
              </a>"""
    content = re.sub(
        r'<div class="main-footer__social-cont">.*?</div>',
        f'<div class="main-footer__social-cont">\n{footer_socials}\n            </div>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 4. Contact Form action
    content = re.sub(
        r'<form action="#" class="contact__form">',
        '<form action="https://formspree.io/f/YOUR_ID_HERE" method="POST" class="contact__form">',
        content
    )

    # 5. Footer Credits
    footer_credits = """&copy; Copyright <span id="year"></span>. Made by
          <a rel="noreferrer" target="_blank" href="https://github.com/givemehat">Rajnish Singh</a>"""
    content = re.sub(
        r'&copy; Copyright 2021\. Made by\s*<a rel="noreferrer" target="_blank" href="https://rammaheshwari\.com"\s*>Rajnish Singh</a\s*>',
        footer_credits,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

for f in html_files:
    if os.path.exists(f):
        update_file(f)

