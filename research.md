<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Essoham ALI — Research</title>

  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      margin: 0;
      background-color: #ffffff;
      color: #222;
    }

    /* ===== TITRE ===== */
    .site-title {
      font-size: 36px;
      font-weight: normal;
      color: #2a7dbb;
      max-width: 1200px;
      margin: 25px auto 15px auto;
      padding: 0 10px;
    }

    /* ===== IMAGE PANORAMIQUE ===== */
    .banner {
      width: 100%;
      margin-bottom: 30px;
      border-top: 4px solid #d0d8de;
    }
    .banner img {
      width: 100%;
      height: 300px;
      object-fit: cover;
      display: block;
    }

    /* ===== LAYOUT PRINCIPAL ===== */
    .container {
      display: flex;
      max-width: 1200px;
      margin: 0 auto 40px auto;
      padding: 0 10px;
    }

    /* ===== MENU ===== */
    nav {
      width: 200px;
      margin-right: 30px;
    }
    nav a {
      display: block;
      padding: 12px;
      margin-bottom: 10px;
      background-color: #eee;
      color: #333;
      text-decoration: none;
      font-weight: bold;
      border-left: 6px solid transparent;
    }
    nav a:hover { background-color: #ddd; }

    /* Onglet actif */
    nav a.active {
      border-left-color: #2a7dbb;
      background-color: #e6eef6;
    }

    /* ===== CONTENU ===== */
    main { flex: 1; }

    h2 {
      color: #2a7dbb;
      margin-top: 10px;
      font-size: 26px;
    }

    h3 {
      color: #2a7dbb;
      margin-top: 22px;
      font-size: 20px;
    }

    p { line-height: 1.6; }

    ul.pub-list {
      margin: 10px 0 0 18px;
      padding: 0;
    }
    ul.pub-list li {
      margin: 8px 0;
      line-height: 1.5;
    }

    /* ===== FOOTER ===== */
    .site-footer {
      margin-top: 60px;
      padding: 30px 10px;
      border-top: 1px dotted #ccc;
      text-align: center;
      font-size: 14px;
      color: #777;
    }
    .site-footer p { margin: 5px 0; }
    .footer-credit { color: #999; }

    /* ===== RESPONSIVE SIMPLE ===== */
    @media (max-width: 800px) {
      .container { flex-direction: column; }
      nav { width: 100%; margin-bottom: 20px; }
    }
  </style>
</head>

<body>

  <!-- TITRE -->
  <h1 class="site-title">Essoham ALI</h1>

  <!-- IMAGE PANORAMIQUE -->
  <div class="banner">
    <img src="panorama.png" alt="Panorama">
  </div>

  <!-- CONTENU PRINCIPAL -->
  <div class="container">

    <nav>
      <a href="index.html">HOME</a>
      <a href="cv.html">CV</a>
      <a class="active" href="research.html">RESEARCH</a>
      <a href="talks.html">TALKS</a>
      <a href="teaching.html">TEACHING</a>
    </nav>

    <main>
      <h2>RESEARCH</h2>

      <h3>Publications</h3>
   
      <h3>Articles (Statistics)</h3>
      <ul class="pub-list">
        <!-- Mets ici ta liste d’articles en statistiques -->
       <li>
  <strong>Ali, E., Lukman, A.F. &amp; Manou-Abi, S.M.</strong>.
  Regularized estimation for right-censored zero-inflated poisson regression:
  methods and applications to health data.
  <em class="journal">
    <a href="https://link.springer.com/article/10.1007/s00180-025-01675-6" target="_blank">
      Computational Statistics
    </a>
  </em>,
  41(18), 2026.
</li>

  <li>
  <strong>Lukman, A.F., Ali, E.</strong>
  Contraction Ridge Estimator: Simulation and Application to Economic Data.
  <em class="journal">
    <a href="https://link.springer.com/article/10.1007/s10614-025-11182-x" target="_blank">
      Computational Economics
    </a>
  </em> 
    to appear, 2025.
  </li>

        <li>
  <strong>Ali, E., &amp; Lukman, A. F.</strong>.
  Ridge-penalized Zero-Inflated Probit Bell model for multicollinearity in count data.
  <em class="journal">
    <a href="https://www.tandfonline.com/doi/full/10.1080/02664763.2025.2530551" target="_blank">
      Journal of Applied Statistics
    </a>
  </em>,
  to appear, 2025.
</li>

        <li>
  <strong>Ali, E., &amp; Pho, K. H.</strong>.
  A novel model for count data: zero-inflated Probit Bell model with applications.
  <em class="journal">
    <a href="https://www.tandfonline.com/doi/full/10.1080/03610918.2024.2384574" target="_blank">
      Communications in Statistics – Simulation and Computation
    </a>
  </em>,
  54(11), 4586–4604, 2025.
</li>

<li>
  <strong>Ali, E.</strong>.
  A simulation-based study of ZIP regression with various zero-inflated submodels.
  <em class="journal">
    <a href="https://www.tandfonline.com/doi/full/10.1080/03610918.2022.2025840" target="_blank">
      Communications in Statistics – Simulation and Computation
    </a>
  </em>,
  53(2), 642–657, 2024.
</li>

<li>
  <strong>Ali, E., Diop, M. L., &amp; Diop, A.</strong>.
  Statistical Inference in a Zero-Inflated Bell Regression Model.
  <em class="journal">
    <a href="https://link.springer.com/article/10.3103/S1066530722030012" target="_blank">
      Mathematical Methods of Statistics
    </a>
  </em>,
  31, 91–104, 2022.
</li>
<li>
  <strong>Ali, E., Diop, A., &amp; Dupuy, J. F.</strong>.
  A constrained marginal zero-inflated binomial regression model.
  <em class="journal">
    <a href="https://www.tandfonline.com/doi/full/10.1080/03610926.2020.1861296" target="_blank">
      Communications in Statistics – Theory and Methods
    </a>
  </em>,
  51(18), 6396–6422, 2022.
</li>

      </ul>

      <h3>Articles (Applications / Engineering)</h3>
      <ul class="pub-list">
        <!-- Mets ici ta liste d’articles appliqués -->
        <li><strong>Auteur(s)</strong>. Titre de l’article. <em>Journal</em>, volume(numéro), pages, année.</li>
      </ul>

      <h3>Short notes</h3>
      <ul class="pub-list">
        <li><strong>Auteur(s)</strong>. Titre. <em>Revue</em>, année.</li>
      </ul>


      <h3>Submitted / Preprints</h3>
      <ul class="pub-list">
        <li><strong>Auteur(s)</strong>. Titre. Preprint / HAL / arXiv : identifiant.</li>
      </ul>

    </main>
  </div>

  <!-- FOOTER -->
  <footer class="site-footer">
    <p>© 2023 Essoham Ali </p>
    <p class="footer-credit">Template design by Andreas Viklund</p>
  </footer>

</body>
</html>
