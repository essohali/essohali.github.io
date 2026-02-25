---
layout: default
title: Home
---

<div class="hero">

  <!-- ================= FR ================= -->
  <div class="lang fr">

    <div class="profile-card">
      <img src="/assets/profile.jpg" alt="Essoham Ali">

      <div class="profile-meta">
        <p class="name">Essoham Ali</p>
        <p class="role">
          Maître de conférences — UCO Angers<br>
          Institut de mathématiques appliquées (MAI)
        </p>

        <ul>
          <li>Statistiques appliquées pour données de comptage complexes</li>
          <li>Modèles zéro-inflationnés & inférence statistique</li>
          <li>Régularisation et estimation pénalisée</li>
          <li>Applications : santé et économie</li>
        </ul>
      </div>
    </div>

    <div class="hero-right">
      <h1>Profil de recherche</h1>

      <p>
        Je développe des outils méthodologiques en
        <strong>statistiques appliquées</strong> et
        <strong>apprentissage statistique</strong>,
        avec un accent particulier sur l’analyse de
        <strong>données complexes et zéro-inflationnées</strong>.
      </p>

      <p>
        Mes travaux combinent modélisation statistique,
        estimation régularisée et méthodes d’inférence,
        motivés par des applications en santé,
        économie et analyse de données réelles.
      </p>

      <p>
        Mes contributions récentes incluent le développement
        de nouveaux modèles pour données de comptage
        (Bell/Probit Bell zéro-inflationnés),
        des procédures d’estimation régularisée pour
        la régression censurée zéro-inflationnée,
        ainsi que des estimateurs ridge/contraction
        pour la multicolinéarité.
      </p>

      <div class="section">
        <h2>Accès rapide</h2>
        <ul>
          <li><a href="/publications/">Publications complètes</a></li>
          <li><a href="/research-vision/">Vision scientifique</a></li>
          <li><a href="/teaching/">Enseignement</a></li>
          <li><a href="/impact/">Impact & applications</a></li>
        </ul>
      </div>
    </div>

  </div>


  <!-- ================= EN ================= -->
  <div class="lang en">

    <div class="profile-card">
      <img src="/assets/profile.jpg" alt="Essoham Ali">

      <div class="profile-meta">
        <p class="name">Essoham Ali</p>
        <p class="role">
          Associate Professor (Maître de conférences) — UCO Angers<br>
          Institute of Applied Mathematics (MAI)
        </p>

        <ul>
          <li>Applied statistics for complex count data</li>
          <li>Zero-inflated models & statistical inference</li>
          <li>Regularization and penalized estimation</li>
          <li>Applications: health and economics</li>
        </ul>
      </div>
    </div>

    <div class="hero-right">
      <h1>Research profile</h1>

      <p>
        I develop methodological tools in
        <strong>applied statistics and statistical learning</strong>,
        with a focus on analysing
        <strong>complex and zero-inflated data</strong>.
      </p>

      <p>
        My research combines statistical modelling,
        regularized estimation, and inference methods,
        motivated by applications in health sciences,
        economics, and real-world data analysis.
      </p>

      <p>
        Recent contributions include new probabilistic models
        for count data (zero-inflated Bell/Probit Bell models),
        regularized estimation procedures for censored
        zero-inflated regression, and ridge/contraction
        estimators addressing multicollinearity.
      </p>
<div id="fr">
  <div class="section">
    <h2>Recherches récentes</h2>

    <h3>Axe 1 — Données de comptage multivariées : dépendance, sur-dispersion et interprétabilité</h3>
    <p>
      Je développe des modèles pour <strong>données de comptage multivariées corrélées</strong> (dépendance entre composantes + sur-dispersion),
      en proposant une <strong>décomposition interprétable</strong> “partagée vs idiosyncratique” via des modèles de fragilité.
      L’objectif est de <strong>séparer</strong> ce qui relève de la dépendance globale et ce qui relève de l’hétérogénéité spécifique à chaque variable,
      avec une <strong>identifiabilité</strong> établie et une <strong>inférence EM</strong>.
    </p>
    <ul>
      <li><strong>Thèmes :</strong> modèles mixtes Poisson, fragilité partagée/idiosyncratique, identifiabilité, dépendance (au-delà de la corrélation), EM.</li>
      <li><strong>Applications :</strong> données biomédicales et données réelles corrélées (comptage longitudinal/multivarié).</li>
      <li><strong>Papier :</strong> <em>Shared–idiosyncratic frailty models for multivariate count data</em>. </li>
    </ul>

    <h3>Axe 2 — Sélection de variables robuste en grande dimension : single-index models et contamination</h3>
    <p>
      Je m’intéresse à la <strong>sélection de variables</strong> et la <strong>réduction de dimension</strong> pour des modèles semi-paramétriques (single-index),
      en contexte <strong>high-dimensional</strong> et <strong>données contaminées</strong> (observations influentes, points de levier, erreurs à queue lourde).
      Nous proposons une méthode <strong>doublement robuste</strong> combinant <strong>régression médiane locale pénalisée</strong> et
      une synthèse <strong>faible-rang et parcimonieuse</strong> (SOPG-LAD).
    </p>
    <ul>
      <li><strong>Thèmes :</strong> robustesse, observations influentes, sélection de variables, pénalisation ℓ1, gradients locaux, SDR (sufficient dimension reduction).</li>
      <li><strong>Applications :</strong> pollution de l’air, sélection de gènes (p ≫ n).</li>
      <li><strong>Papier :</strong> <em>Doubly-robust sufficient variable selection in single-index models with outlier contaminations</em>. </li>
    </ul>
  </div>
</div>

<div id="en" style="display:none;">
  <div class="section">
    <h2>Recent research</h2>

    <h3>Axis 1 — Multivariate count data: dependence, overdispersion, and interpretability</h3>
    <p>
      I develop models for <strong>correlated multivariate count data</strong> (cross-sectional dependence and marginal overdispersion),
      introducing an <strong>interpretable shared–idiosyncratic decomposition</strong> through frailty modeling.
      The goal is to <strong>separate</strong> global dependence from outcome-specific heterogeneity,
      with <strong>formal identifiability</strong> and <strong>EM-based inference</strong>.
    </p>
    <ul>
      <li><strong>Themes:</strong> mixed Poisson models, shared/idiosyncratic frailties, identifiability, dependence beyond correlation, EM algorithm.</li>
      <li><strong>Applications:</strong> biomedical and real-world correlated count data (multivariate/longitudinal settings).</li>
      <li><strong>Paper:</strong> <em>Shared–idiosyncratic frailty models for multivariate count data</em>. </li>
    </ul>

    <h3>Axis 2 — Robust high-dimensional variable selection: single-index models under contamination</h3>
    <p>
      I work on <strong>variable selection</strong> and <strong>sufficient dimension reduction</strong> for semi-parametric single-index models,
      in <strong>high-dimensional</strong> settings with <strong>contaminated data</strong> (influential points, leverage points, heavy-tailed errors).
      We propose a <strong>doubly robust</strong> method combining <strong>penalized local median regression</strong> with
      <strong>sparse low-rank</strong> summarization (SOPG-LAD).
    </p>
    <ul>
      <li><strong>Themes:</strong> robustness, influential observations, variable selection, ℓ1-penalization, local gradients, SDR.</li>
      <li><strong>Applications:</strong> air pollution, gene selection (p ≫ n).</li>
      <li><strong>Paper:</strong> <em>Doubly-robust sufficient variable selection in single-index models with outlier contaminations</em>. </li>
    </ul>
  </div>
</div>

<script>
  // Simple toggle if you keep your FR|EN links as #fr and #en
  function showLangFromHash() {
    const h = (window.location.hash || "#fr").toLowerCase();
    const fr = document.getElementById("fr");
    const en = document.getElementById("en");
    if (!fr || !en) return;
    if (h === "#en") { fr.style.display = "none"; en.style.display = "block"; }
    else { en.style.display = "none"; fr.style.display = "block"; }
  }
  window.addEventListener("hashchange", showLangFromHash);
  showLangFromHash();
</script>
      <div class="section">
        <h2>Quick access</h2>
        <ul>
          <li><a href="/publications/">Selected & full publications</a></li>
          <li><a href="/research-vision/">Research vision</a></li>
          <li><a href="/teaching/">Teaching activities</a></li>
          <li><a href="/impact/">Impact & applications</a></li>
        </ul>
      </div>
    </div>

  </div>

</div>


<div class="section lang fr">
  <h2>Mots-clés</h2>
  <p>
    Régression zéro-inflationnée · Données de comptage · Estimation pénalisée ·
    Régularisation ridge · Inférence statistique · Modélisation appliquée
  </p>
</div>

<div class="section lang en">
  <h2>Keywords</h2>
  <p>
    Zero-inflated regression · Count data · Penalized estimation ·
    Ridge regularization · Statistical inference · Applied modelling
  </p>
</div>
