with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

sections = """
    <section id="certifications" class="about sec-pad">
      <div class="main-container">
        <h2 class="heading heading-sec heading-sec__mb-med">
          <span class="heading-sec__main">Certifications</span>
          <span class="heading-sec__sub">
            Continuous learning and official recognition of my skills.
          </span>
        </h2>
        <div class="about__content">
          <div class="about__content-main">
            <h3 class="about__content-title">Licenses & Certifications</h3>
            <div class="about__content-details">
              <p class="about__content-details-para">
                <strong>IBM Qiskit Advocate</strong> - IBM Quantum<br/>
                <strong>McKinsey Forward Program</strong> - McKinsey & Company<br/>
                <em>(More certifications available on my LinkedIn profile)</em>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="publications" class="about sec-pad" style="background-color: #fafafa;">
      <div class="main-container">
        <h2 class="heading heading-sec heading-sec__mb-med">
          <span class="heading-sec__main">Publications</span>
          <span class="heading-sec__sub">
            Academic research and published papers in AI & Computer Vision.
          </span>
        </h2>
        <div class="about__content">
          <div class="about__content-main">
            <h3 class="about__content-title">Research Papers</h3>
            <div class="about__content-details">
              <p class="about__content-details-para">
                <strong>Restoring Damaged Indian Folk Art Using Deep Learning</strong><br/>
                Published research on restoring damaged cultural imagery using advanced Deep Learning and Computer Vision techniques.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# Inject before the projects section
target_str = '    <section id="projects" class="projects sec-pad">'
content = content.replace(target_str, sections + target_str)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
