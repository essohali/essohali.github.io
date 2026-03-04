<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Essoham Ali — Lecturer–Researcher in Statistics</title>
  <meta name="description" content="Essoham Ali — Lecturer–Researcher in Statistics. Research in count data models, zero-inflated processes, and high-dimensional inference." />
  <meta name="theme-color" content="#0b1220" />

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">

  <style>
    :root{
      --bg: #0b1220;
      --panel: rgba(255,255,255,.06);
      --panel2: rgba(255,255,255,.08);
      --text: rgba(255,255,255,.92);
      --muted: rgba(255,255,255,.72);
      --muted2: rgba(255,255,255,.58);
      --line: rgba(255,255,255,.12);
      --brand1:#7c3aed; /* violet */
      --brand2:#22c55e; /* green */
      --brand3:#38bdf8; /* sky */
      --shadow: 0 18px 60px rgba(0,0,0,.45);
      --radius: 18px;
      --radius2: 26px;
      --max: 1120px;
    }
    *{ box-sizing:border-box; }
    html,body{ height:100%; }
    body{
      margin:0;
      font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      color: var(--text);
      background:
        radial-gradient(900px 500px at 15% 10%, rgba(124,58,237,.35), transparent 60%),
        radial-gradient(700px 500px at 70% 20%, rgba(56,189,248,.22), transparent 65%),
        radial-gradient(900px 600px at 80% 80%, rgba(34,197,94,.16), transparent 60%),
        linear-gradient(180deg, #060a14 0%, #0b1220 55%, #070b15 100%);
      overflow-x:hidden;
    }
    a{ color: inherit; text-decoration:none; }
    .wrap{ max-width: var(--max); margin: 0 auto; padding: 0 20px; }
    .topbar{
      position: sticky; top:0; z-index: 50;
      backdrop-filter: blur(10px);
      background: rgba(7,10,18,.55);
      border-bottom: 1px solid var(--line);
    }
    .nav{
      display:flex; align-items:center; justify-content:space-between;
      padding: 14px 0;
      gap: 12px;
    }
    .brand{
      display:flex; align-items:center; gap:10px;
      font-weight:700;
      letter-spacing:.2px;
    }
    .logo{
      width: 36px; height: 36px; border-radius: 12px;
      background:
        radial-gradient(12px 12px at 30% 30%, rgba(255,255,255,.35), transparent 60%),
        linear-gradient(135deg, rgba(124,58,237,.95), rgba(56,189,248,.9));
      box-shadow: 0 10px 22px rgba(124,58,237,.22);
      border: 1px solid rgba(255,255,255,.16);
    }
    .navlinks{
      display:flex; align-items:center; gap: 18px;
      color: var(--muted);
      font-weight: 600;
      font-size: 14px;
    }
    .navlinks a{
      padding: 9px 10px; border-radius: 12px;
      transition: .18s ease;
    }
    .navlinks a:hover{ background: rgba(255,255,255,.06); color: var(--text); }
    .cta{
      display:flex; align-items:center; gap: 10px;
    }
    .btn{
      border: 1px solid rgba(255,255,255,.14);
      background: rgba(255,255,255,.06);
      color: var(--text);
      padding: 10px 14px;
      border-radius: 14px;
      font-weight: 700;
      font-size: 14px;
      cursor:pointer;
      transition: transform .16s ease, background .16s ease, border-color .16s ease;
      display:inline-flex; align-items:center; gap:10px;
    }
    .btn:hover{ transform: translateY(-1px); background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.22); }
    .btn.primary{
      border-color: rgba(124,58,237,.45);
      background: linear-gradient(135deg, rgba(124,58,237,.92), rgba(56,189,248,.7));
      box-shadow: 0 18px 40px rgba(124,58,237,.2);
    }
    .btn.primary:hover{ background: linear-gradient(135deg, rgba(124,58,237,.98), rgba(56,189,248,.76)); }
    .chip{
      display:inline-flex; align-items:center; gap: 8px;
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,.14);
      background: rgba(255,255,255,.06);
      color: var(--muted);
      font-weight: 700;
      font-size: 13px;
    }
    .hero{
      padding: 52px 0 26px;
      position: relative;
    }
    .heroGrid{
      display:grid;
      grid-template-columns: 1.25fr .75fr;
      gap: 18px;
      align-items: stretch;
    }
    .card{
      border: 1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.06);
      border-radius: var(--radius2);
      box-shadow: var(--shadow);
      overflow:hidden;
    }
    .cardInner{ padding: 26px; }
    h1{
      font-family: "Playfair Display", serif;
      font-weight: 700;
      margin: 10px 0 8px;
      font-size: clamp(32px, 4vw, 52px);
      line-height: 1.05;
      letter-spacing: .2px;
    }
    .subtitle{
      color: var(--muted);
      font-size: 16px;
      line-height: 1.55;
      margin: 0 0 18px;
      max-width: 62ch;
    }
    .meta{
      display:flex; flex-wrap:wrap; gap: 10px;
      margin: 16px 0 10px;
    }
    .meta .chip strong{ color: var(--text); }
    .heroActions{
      display:flex; flex-wrap:wrap; gap: 10px;
      margin-top: 16px;
    }
    .side{
      display:flex; flex-direction:column; gap: 12px;
    }
    .mini{
      border-radius: var(--radius2);
      border: 1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.06);
      box-shadow: var(--shadow);
      padding: 18px;
    }
    .mini h3{
      margin: 0 0 6px;
      font-size: 14px;
      letter-spacing: .4px;
      text-transform: uppercase;
      color: var(--muted);
    }
    .mini p, .mini a{
      margin:0;
      color: var(--text);
      font-weight: 700;
      line-height: 1.45;
      word-break: break-word;
    }
    .mini small{ display:block; margin-top: 6px; color: var(--muted2); line-height: 1.5; }
    .grid3{
      display:grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }
    .section{
      padding: 26px 0;
    }
    .sectionHeader{
      display:flex; align-items:end; justify-content:space-between; gap: 14px;
      margin-bottom: 12px;
    }
    .sectionTitle{
      font-family: "Playfair Display", serif;
      font-size: 26px;
      margin:0;
    }
    .sectionNote{
      margin:0;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.5;
      max-width: 60ch;
    }
    .panel{
      border: 1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.05);
      border-radius: var(--radius2);
      padding: 18px;
      box-shadow: 0 14px 45px rgba(0,0,0,.32);
    }
    .panel h4{
      margin: 0 0 10px;
      font-size: 16px;
      color: var(--text);
    }
    .bullets{
      display:grid;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
      color: var(--muted);
      line-height: 1.55;
    }
    .bullets li{
      display:flex; gap: 10px; align-items:flex-start;
    }
    .dot{
      width: 10px; height: 10px; margin-top: 7px;
      border-radius: 999px;
      background: linear-gradient(135deg, var(--brand1), var(--brand3));
      box-shadow: 0 10px 25px rgba(124,58,237,.22);
      flex: 0 0 auto;
    }

    .pub{
      display:grid; gap: 12px;
    }
    .pubItem{
      border: 1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.06);
      border-radius: var(--radius);
      padding: 16px;
      transition: transform .16s ease, background .16s ease, border-color .16s ease;
    }
    .pubItem:hover{
      transform: translateY(-2px);
      background: rgba(255,255,255,.08);
      border-color: rgba(255,255,255,.2);
    }
    .pubItem .where{
      display:flex; justify-content:space-between; gap: 12px;
      color: var(--muted2);
      font-weight: 700;
      font-size: 13px;
      margin-bottom: 6px;
    }
    .pubItem .title{
      margin:0;
      font-weight: 800;
      line-height: 1.35;
    }
    .pubItem .authors{
      margin: 8px 0 0;
      color: var(--muted);
      line-height: 1.5;
    }

    .keywords{
      display:flex; flex-wrap:wrap; gap: 10px;
      margin-top: 10px;
    }
    .tag{
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.05);
      color: var(--muted);
      font-weight: 700;
      font-size: 13px;
      transition: .16s ease;
    }
    .tag:hover{ background: rgba(255,255,255,.07); color: var(--text); }

    footer{
      padding: 28px 0 36px;
      border-top: 1px solid var(--line);
      color: var(--muted2);
    }
    .foot{
      display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap: 12px;
      font-size: 13px;
    }

    /* Simple reveal animation */
    .reveal{ opacity: 0; transform: translateY(10px); transition: opacity .5s ease, transform .5s ease; }
    .reveal.show{ opacity: 1; transform: translateY(0); }

    /* Responsive */
    @media (max-width: 980px){
      .heroGrid{ grid-template-columns: 1fr; }
      .grid3{ grid-template-columns: 1fr; }
      .navlinks{ display:none; }
    }
  </style>
</head>

<body>
  <!-- Topbar -->
  <header class="topbar">
    <div class="wrap">
      <div class="nav">
        <a class="brand" href="#top" aria-label="Accueil">
          <span class="logo" aria-hidden="true"></span>
          <span>Essoham Ali</span>
        </a>

        <nav class="navlinks" aria-label="Navigation">
          <a href="#profile">Research Profile</a>
          <a href="#interests">Research Interests</a>
          <a href="#publications">Publications</a>
          <a href="#computing">Computational</a>
          <a href="#keywords">Keywords</a>
        </nav>

        <div class="cta">
          <a class="btn" href="mailto:essoham.ali@univ-ubs.fr" title="Envoyer un email">✉️ Contact</a>
          <a class="btn primary" href="#publications" title="Voir les publications">📚 Publications</a>
        </div>
      </div>
    </div>
  </header>

  <!-- Hero -->
  <main id="top" class="hero">
    <div class="wrap">
      <div class="heroGrid">
        <section class="card reveal" aria-label="Présentation">
          <div class="cardInner">
            <span class="chip">📌 <strong>Home</strong> — version optimisée (MCF section 26)</span>
            <h1>Essoham Ali</h1>
            <p class="subtitle">
              <strong>Lecturer–Researcher in Statistics</strong><br/>
              Institute of Applied Mathematics (MAI), UCO Angers<br/>
              Member of LMBA – Université Bretagne Sud
            </p>

            <div class="meta">
              <span class="chip">🧮 <strong>Statistics</strong> • Modelling & Inference</span>
              <span class="chip">🔎 <strong>Count Data</strong> • Zero-inflation • Dependence</span>
              <span class="chip">📈 <strong>High-Dimensional</strong> • Penalization • Selection</span>
            </div>

            <div class="heroActions">
              <a class="btn primary" href="mailto:essoham.ali@univ-ubs.fr">✉️ essoham.ali@univ-ubs.fr</a>
              <a class="btn" href="#profile">➡️ Research Profile</a>
              <a class="btn" href="#interests">✨ Research Interests</a>
            </div>

            <p class="subtitle" style="margin-top:16px;color:var(--muted2)">
              I develop probabilistically grounded statistical models and regularized estimation procedures
              for structured and high-dimensional datasets, with applications in health sciences,
              economics, and data-driven scientific studies.
            </p>
          </div>
        </section>

        <aside class="side">
          <div class="mini reveal">
            <h3>Contact</h3>
            <p><a href="mailto:essoham.ali@univ-ubs.fr">📧 essoham.ali@univ-ubs.fr</a></p>
            <small>For collaborations, student supervision, and research discussions.</small>
          </div>

          <div class="mini reveal">
            <h3>Affiliations</h3>
            <p>MAI — UCO Angers</p>
            <small>Member of LMBA — Université Bretagne Sud</small>
          </div>

          <div class="mini reveal">
            <h3>Focus</h3>
            <p>Zero-inflated count processes</p>
            <small>Flexible dependence modelling & high-dimensional inference.</small>
          </div>
        </aside>
      </div>
    </div>
  </main>

  <!-- Research Profile -->
  <section id="profile" class="section">
    <div class="wrap">
      <div class="sectionHeader">
        <h2 class="sectionTitle">Research Profile</h2>
        <p class="sectionNote">
          Statistical modelling & inference for complex data, focusing on count data, zero inflation,
          and high-dimensional methods.
        </p>
      </div>

      <div class="panel reveal">
        <ul class="bullets">
          <li><span class="dot"></span><span>
            My research focuses on <strong>statistical modelling and inference</strong> for complex data,
            with an emphasis on <strong>count data models</strong>, <strong>zero-inflated processes</strong>,
            and <strong>high-dimensional statistical methods</strong>.
          </span></li>
          <li><span class="dot"></span><span>
            I develop <strong>probabilistically grounded models</strong> and <strong>regularized estimation procedures</strong>
            to handle structured and high-dimensional datasets in modern applications.
          </span></li>
          <li><span class="dot"></span><span>
            A central theme is modelling <strong>dependent count data</strong> with flexible models capturing
            <strong>overdispersion</strong>, <strong>excess zeros</strong>, and complex <strong>dependence structures</strong>.
          </span></li>
          <li><span class="dot"></span><span>
            Methodologically, my work combines <strong>mathematical statistics</strong>, <strong>statistical learning</strong>,
            and <strong>computational statistics</strong>, studying properties such as
            <strong>consistency</strong>, <strong>robustness</strong>, and <strong>oracle properties</strong>.
          </span></li>
          <li><span class="dot"></span><span>
            Applications include <strong>health sciences</strong>, <strong>economics</strong>, and <strong>data-driven scientific studies</strong>,
            where interpretability and reliable inference are essential.
          </span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Research Interests -->
  <section id="interests" class="section">
    <div class="wrap">
      <div class="sectionHeader">
        <h2 class="sectionTitle">Research Interests</h2>
        <p class="sectionNote">A structured overview of my main research directions.</p>
      </div>

      <div class="grid3">
        <div class="panel reveal">
          <h4>Statistical Modelling</h4>
          <ul class="bullets">
            <li><span class="dot"></span><span>Count data models</span></li>
            <li><span class="dot"></span><span>Zero-inflated and mixture models</span></li>
            <li><span class="dot"></span><span>Multivariate dependence modelling</span></li>
          </ul>
        </div>

        <div class="panel reveal">
          <h4>High-Dimensional Inference</h4>
          <ul class="bullets">
            <li><span class="dot"></span><span>Penalized regression</span></li>
            <li><span class="dot"></span><span>Variable selection</span></li>
            <li><span class="dot"></span><span>Robust statistical inference</span></li>
          </ul>
        </div>

        <div class="panel reveal">
          <h4>Computational Statistics</h4>
          <ul class="bullets">
            <li><span class="dot"></span><span>Simulation-based statistical methods</span></li>
            <li><span class="dot"></span><span>Numerical estimation procedures</span></li>
            <li><span class="dot"></span><span>Statistical learning algorithms</span></li>
          </ul>
        </div>
      </div>

      <div class="panel reveal" style="margin-top:14px">
        <h4>Applications</h4>
        <div class="keywords">
          <span class="tag">Health sciences</span>
          <span class="tag">Economics</span>
          <span class="tag">Data science</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Selected Publications -->
  <section id="publications" class="section">
    <div class="wrap">
      <div class="sectionHeader">
        <h2 class="sectionTitle">Selected Publications</h2>
        <p class="sectionNote">A selection of recent work (as listed on this page).</p>
      </div>

      <div class="pub">
        <article class="pubItem reveal">
          <div class="where">
            <span>Computational Statistics</span>
            <span>2026</span>
          </div>
          <p class="title">Regularized estimation for right-censored zero-inflated Poisson regression: methods and applications to health data.</p>
          <p class="authors">Ali, E., Lukman, A. F., &amp; Manou-Abi, S. M.</p>
        </article>

        <article class="pubItem reveal">
          <div class="where">
            <span>Journal of Applied Statistics</span>
            <span>2025</span>
          </div>
          <p class="title">Penalized zero-inflated Bell regression for multicollinearity in count data.</p>
          <p class="authors">Ali, E., &amp; Lukman, A. F.</p>
        </article>

        <article class="pubItem reveal">
          <div class="where">
            <span>Communications in Statistics – Simulation and Computation</span>
            <span>2025</span>
          </div>
          <p class="title">A new zero-inflated Bell model for count data with applications.</p>
          <p class="authors">Ali, E., &amp; Pho, K. H.</p>
        </article>
      </div>

      <div class="heroActions" style="margin-top:14px">
        <a class="btn" href="#computing">🧪 Computational materials</a>
        <a class="btn" href="mailto:essoham.ali@univ-ubs.fr?subject=Collaboration%20Inquiry">🤝 Collaboration</a>
      </div>
    </div>
  </section>

  <!-- Computational -->
  <section id="computing" class="section">
    <div class="wrap">
      <div class="sectionHeader">
        <h2 class="sectionTitle">Computational Statistics &amp; Data Science</h2>
        <p class="sectionNote">
          Tools, simulation studies, and reproducible experiments illustrating modern methodology.
        </p>
      </div>

      <div class="panel reveal">
        <p style="margin:0;color:var(--muted);line-height:1.65">
          Part of my research also involves the development of computational tools and simulation studies for statistical models used in the analysis of complex data.
          Example materials available on this website include:
        </p>

        <div class="grid3" style="margin-top:14px">
          <div class="pubItem" style="box-shadow:none">
            <p class="title">Simulation studies</p>
            <p class="authors">Reproducible experiments for zero-inflated models.</p>
          </div>
          <div class="pubItem" style="box-shadow:none">
            <p class="title">High-dimensional regression</p>
            <p class="authors">Penalized estimation &amp; selection under structured data.</p>
          </div>
          <div class="pubItem" style="box-shadow:none">
            <p class="title">R &amp; Python examples</p>
            <p class="authors">Implementations of statistical learning workflows.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Keywords -->
  <section id="keywords" class="section">
    <div class="wrap">
      <div class="sectionHeader">
        <h2 class="sectionTitle">Keywords</h2>
        <p class="sectionNote">Main topics and themes.</p>
      </div>

      <div class="panel reveal">
        <div class="keywords">
          <span class="tag">Mathematical Statistics</span>
          <span class="tag">Statistical Learning</span>
          <span class="tag">Computational Statistics</span>
          <span class="tag">High-Dimensional Inference</span>
          <span class="tag">Count Data Models</span>
          <span class="tag">Probability Models</span>
          <span class="tag">Data Science</span>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="wrap">
      <div class="foot">
        <span>© <span id="year"></span> Essoham Ali — Academic Homepage</span>
        <span style="color:var(--muted)">Built with clean HTML/CSS • Responsive • Lightweight</span>
      </div>
    </div>
  </footer>

  <script>
    // Year
    document.getElementById("year").textContent = new Date().getFullYear();

    // Reveal on scroll
    const els = document.querySelectorAll(".reveal");
    const io = new IntersectionObserver((entries)=>{
      for(const e of entries){
        if(e.isIntersecting) e.target.classList.add("show");
      }
    }, { threshold: 0.12 });
    els.forEach(el => io.observe(el));

    // Smooth anchor scroll
    document.querySelectorAll('a[href^="#"]').forEach(a=>{
      a.addEventListener("click", (ev)=>{
        const id = a.getAttribute("href");
        if(!id || id === "#") return;
        const target = document.querySelector(id);
        if(!target) return;
        ev.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  </script>
</body>
</html>
