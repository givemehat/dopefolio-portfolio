with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_projects = """
          <div class="projects__row">
            <div class="projects__row-img-cont">
              <img
                src="./assets/jpeg/qdms_thumbnail.jpg"
                alt="AlphaGrep Securities"
                class="projects__row-img"
                loading="lazy"
              />
            </div>
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">AlphaGrep Volatility Forecasting</h3>
              <p class="projects__row-content-desc">Engineered high-frequency volatility forecasting and options liquidity models for quantitative research at AlphaGrep Securities.</p>
              <a href="#" class="btn btn--med btn--theme dynamicBgClr" target="_blank">Case Study</a>
            </div>
          </div>
          <div class="projects__row">
            <div class="projects__row-img-cont">
              <img
                src="./assets/jpeg/aiml_capstone.jpg"
                alt="AUV Battery RUL"
                class="projects__row-img"
                loading="lazy"
              />
            </div>
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">AUV Battery RUL Prediction</h3>
              <p class="projects__row-content-desc">Developed predictive maintenance models for Autonomous Underwater Vehicle (AUV) Battery Remaining Useful Life during an internship at TIH, IIT Guwahati.</p>
              <a href="#" class="btn btn--med btn--theme dynamicBgClr" target="_blank">Case Study</a>
            </div>
          </div>
          <div class="projects__row">
            <div class="projects__row-img-cont">
              <img
                src="./assets/jpeg/devpulse.jpg"
                alt="Autonomous UAV Navigation"
                class="projects__row-img"
                loading="lazy"
              />
            </div>
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">Risk-Aware UAV Navigation</h3>
              <p class="projects__row-content-desc">Built an autonomous, risk-aware Unmanned Aerial Vehicle navigation system utilizing LSTM-based threat assessment algorithms.</p>
              <a href="#" class="btn btn--med btn--theme dynamicBgClr" target="_blank">Case Study</a>
            </div>
          </div>
          <div class="projects__row">
            <div class="projects__row-img-cont">
              <img
                src="./assets/jpeg/qdms_thumbnail.jpg"
                alt="Indian Folk Art Restoration"
                class="projects__row-img"
                loading="lazy"
              />
            </div>
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">Indian Folk Art Restoration</h3>
              <p class="projects__row-content-desc">Published research on restoring damaged Indian folk art imagery using advanced Deep Learning and Computer Vision techniques.</p>
              <a href="#" class="btn btn--med btn--theme dynamicBgClr" target="_blank">Case Study</a>
            </div>
          </div>
          <div class="projects__row">
            <div class="projects__row-img-cont">
              <img
                src="./assets/jpeg/devpulse.jpg"
                alt="HabitFlow"
                class="projects__row-img"
                loading="lazy"
              />
            </div>
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">HabitFlow</h3>
              <p class="projects__row-content-desc">A privacy-first, terminal-based habit tracker designed for developers, ensuring secure and local data storage without telemetry.</p>
              <a href="#" class="btn btn--med btn--theme dynamicBgClr" target="_blank">Case Study</a>
            </div>
          </div>
          <div class="projects__row">
            <div class="projects__row-img-cont">
              <img
                src="./assets/jpeg/aiml_capstone.jpg"
                alt="WhiteCoins Arena"
                class="projects__row-img"
                loading="lazy"
              />
            </div>
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">WhiteCoins Arena</h3>
              <p class="projects__row-content-desc">Developed an interactive multiplayer number-strategy game blending competitive mechanics with algorithmic thinking.</p>
              <a href="#" class="btn btn--med btn--theme dynamicBgClr" target="_blank">Case Study</a>
            </div>
          </div>
"""

# The projects section ends with:
target_end = """        </div>
      </div>
    </section>
    <section id="contact" class="contact sec-pad dynamicBg">"""

replacement = new_projects + target_end
content = content.replace(target_end, replacement)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
