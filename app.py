# app.py
import streamlit as st
from dataclasses import dataclass
from typing import List, Dict, Tuple

# ----------------------------
# Data model
# ----------------------------

@dataclass
class Paper:
    paper_id: str
    title: str
    authors: str
    year: int
    venue: str
    relevance: float
    keywords: List[str]
    snippet: str
    abstract: str


SEED_TITLE = "Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance"
DEFAULT_QUERY_KEY = SEED_TITLE

# ----------------------------
# Papers (core + expanded dummy corpus for deeper chaining)
# ----------------------------

PAPERS: Dict[str, Paper] = {
    # ---- core 8 (same as your set) ----
    "norman_1983": Paper(
        paper_id="norman_1983",
        title="Mental Models of Intelligent Systems",
        authors="D. Norman",
        year=1983,
        venue="Human–Computer Interaction",
        relevance=0.95,
        keywords=["mental models", "human understanding", "cognition"],
        snippet="Introduces mental models as internal representations humans use to understand and predict system behavior.",
        abstract="Classic work describing how people build internal representations of systems to predict outcomes and explain behavior.",
    ),
    "ribeiro_2016_lime": Paper(
        paper_id="ribeiro_2016_lime",
        title="Why Should I Trust You? Explaining the Predictions of Any Classifier",
        authors="M. Ribeiro, S. Singh, C. Guestrin",
        year=2016,
        venue="KDD",
        relevance=0.92,
        keywords=["explainable AI", "interpretability", "trust"],
        snippet="Presents LIME, a method for explaining individual predictions to improve human trust and understanding.",
        abstract="Introduces LIME, a local surrogate explanation method that helps users interpret model predictions and debug behavior.",
    ),
    "kaur_2020_trust": Paper(
        paper_id="kaur_2020_trust",
        title="On the Relationship Between Explanation and Trust in AI Systems",
        authors="S. Kaur et al.",
        year=2020,
        venue="CHI",
        relevance=0.90,
        keywords=["trust", "explainability", "human-AI interaction"],
        snippet="Shows explanations influence trust calibration rather than blind reliance.",
        abstract="Examines how explanation interfaces affect user trust, calibration, and reliance behaviors in AI-assisted tasks.",
    ),
    "amershi_2019_collab": Paper(
        paper_id="amershi_2019_collab",
        title="Human-AI Collaboration: Models, Design Patterns, and Future Directions",
        authors="S. Amershi et al.",
        year=2019,
        venue="CHI",
        relevance=0.93,
        keywords=["human-AI teaming", "collaboration", "design patterns"],
        snippet="Framework for designing effective human-AI collaborative systems beyond raw accuracy.",
        abstract="Synthesizes models and design patterns for human–AI collaboration, emphasizing workflows and feedback loops.",
    ),
    "lipton_2018_mythos": Paper(
        paper_id="lipton_2018_mythos",
        title="The Mythos of Model Interpretability",
        authors="Z. Lipton",
        year=2018,
        venue="Queue",
        relevance=0.85,
        keywords=["interpretability", "mental models", "machine learning"],
        snippet="Critically examines what interpretability means and how it affects user understanding.",
        abstract="Critiques ambiguous definitions of interpretability and argues for clearer goals and evaluation in context.",
    ),
    "bansal_2021_error": Paper(
        paper_id="bansal_2021_error",
        title="Predictability and Transparency in AI Error Behavior",
        authors="H. Bansal, E. Weld",
        year=2021,
        venue="AAAI",
        relevance=0.88,
        keywords=["error boundaries", "predictability", "human-AI teaming"],
        snippet="Predictable error patterns can improve human-AI team performance more than higher accuracy.",
        abstract="Explores how predictable vs. unpredictable errors shape user mental models, reliance, and collaboration outcomes.",
    ),
    "lee_see_2004_trust": Paper(
        paper_id="lee_see_2004_trust",
        title="Appropriate Trust and Reliance in Human-AI Teams",
        authors="J. Lee, K. See",
        year=2004,
        venue="Human Factors",
        relevance=0.87,
        keywords=["trust", "calibration", "automation"],
        snippet="Classic paper on trust calibration and appropriate reliance on automated systems.",
        abstract="Foundational work on trust in automation and how design supports appropriate reliance, avoiding misuse/disuse.",
    ),
    "shneiderman_2020_control": Paper(
        paper_id="shneiderman_2020_control",
        title="Designing AI Systems for Effective Human Control",
        authors="B. Shneiderman",
        year=2020,
        venue="Communications of the ACM",
        relevance=0.84,
        keywords=["human-centered AI", "control", "explainability"],
        snippet="Human-centered design principles to maintain user control and understanding.",
        abstract="Argues for human-centered AI emphasizing oversight, responsibility, and transparency in socio-technical systems.",
    ),

    # ---- existing extra dummy ----
    "doshi_velez_2017": Paper(
        paper_id="doshi_velez_2017",
        title="Towards a Rigorous Science of Interpretable Machine Learning",
        authors="F. Doshi-Velez, B. Kim",
        year=2017,
        venue="(Demo) arXiv",
        relevance=0.82,
        keywords=["interpretability", "evaluation", "machine learning"],
        snippet="Argues for clearer goals and evaluation methods for interpretability.",
        abstract="Proposes a framework for evaluating interpretability depending on task, user population, and stakes.",
    ),
    "miller_2019_explanations": Paper(
        paper_id="miller_2019_explanations",
        title="Explanation in Artificial Intelligence: Insights from the Social Sciences",
        authors="T. Miller",
        year=2019,
        venue="AI Journal",
        relevance=0.83,
        keywords=["explainability", "human understanding", "trust"],
        snippet="Connects explanation needs to how humans understand and accept reasoning.",
        abstract="Synthesizes social science research on explanation and maps implications to AI system design.",
    ),
    "zhang_2020_calibration": Paper(
        paper_id="zhang_2020_calibration",
        title="Calibrating Trust in AI-Assisted Decision Making",
        authors="Y. Zhang et al.",
        year=2020,
        venue="(Demo) CSCW",
        relevance=0.78,
        keywords=["trust", "calibration", "human-AI interaction"],
        snippet="Examines interventions to reduce over/under-reliance on AI.",
        abstract="Studies calibration strategies such as confidence cues, history, and explanations and their effects on reliance.",
    ),
    "wu_2021_error_boundary": Paper(
        paper_id="wu_2021_error_boundary",
        title="Characterizing Error Boundaries for Human-AI Collaboration",
        authors="J. Wu et al.",
        year=2021,
        venue="(Demo) AAAI",
        relevance=0.81,
        keywords=["error boundaries", "human-AI teaming", "predictability"],
        snippet="Ways to summarize failure regions so users can learn when to rely on AI.",
        abstract="Explores representations of error boundaries and how they influence user mental models and reliance behavior.",
    ),
    "khanna_2022_feedback": Paper(
        paper_id="khanna_2022_feedback",
        title="Designing Feedback Loops for Human-AI Teaming",
        authors="S. Khanna et al.",
        year=2022,
        venue="(Demo) CHI",
        relevance=0.77,
        keywords=["human-AI teaming", "collaboration", "design patterns"],
        snippet="Design patterns for feedback loops in human-AI systems.",
        abstract="Discusses feedback loop designs that help humans and AI coordinate, correct errors, and refine strategies.",
    ),
    "yang_2023_transparency": Paper(
        paper_id="yang_2023_transparency",
        title="Transparency Interfaces for Predictable Reliance",
        authors="K. Yang et al.",
        year=2023,
        venue="(Demo) UIST",
        relevance=0.75,
        keywords=["transparency", "trust", "predictability"],
        snippet="UI patterns for communicating limitations and supporting calibrated reliance.",
        abstract="Explores interface patterns that communicate uncertainty and limitations so users can form reliable mental models.",
    ),

    # ---- NEW: mental models / cognition cluster ----
    "johnson_laird_1983": Paper(
        paper_id="johnson_laird_1983",
        title="Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness",
        authors="P. Johnson-Laird",
        year=1983,
        venue="Book (Demo)",
        relevance=0.80,
        keywords=["mental models", "cognition", "reasoning"],
        snippet="Foundational theory describing mental models as the basis for human reasoning and inference.",
        abstract="Proposes that people reason by constructing and manipulating mental models of situations rather than relying on formal logic alone.",
    ),
    "gentner_structure_mapping_1983": Paper(
        paper_id="gentner_structure_mapping_1983",
        title="Structure-Mapping: A Theoretical Framework for Analogy",
        authors="D. Gentner",
        year=1983,
        venue="Cognitive Science (Demo)",
        relevance=0.74,
        keywords=["cognition", "human understanding", "analogy"],
        snippet="Explains how people transfer knowledge via analogical mapping, supporting mental model formation.",
        abstract="Introduces structure-mapping theory of analogy, explaining how relational structure guides human understanding and learning.",
    ),
    "hutchins_cognition_1995": Paper(
        paper_id="hutchins_cognition_1995",
        title="Cognition in the Wild: Distributed Cognition and Real-World Work",
        authors="E. Hutchins",
        year=1995,
        venue="Book (Demo)",
        relevance=0.72,
        keywords=["human understanding", "cognition", "distributed cognition"],
        snippet="Shows cognition is distributed across people and artifacts, relevant to team mental models.",
        abstract="Argues that cognition is not confined to individuals but distributed across social and material systems, shaping performance in complex tasks.",
    ),
    "klein_sensemaking_1998": Paper(
        paper_id="klein_sensemaking_1998",
        title="A Data-Frame Theory of Sensemaking",
        authors="G. Klein et al.",
        year=1998,
        venue="IEEE Intelligent Systems (Demo)",
        relevance=0.70,
        keywords=["sensemaking", "human understanding", "cognition"],
        snippet="Sensemaking theory relevant to how people build and revise mental models.",
        abstract="Describes how people adopt frames to interpret data and revise frames when anomalies arise, explaining how mental models evolve over time.",
    ),
    "endsley_sa_1995": Paper(
        paper_id="endsley_sa_1995",
        title="Toward a Theory of Situation Awareness in Dynamic Systems",
        authors="M. Endsley",
        year=1995,
        venue="Human Factors (Demo)",
        relevance=0.76,
        keywords=["human understanding", "situation awareness", "cognition"],
        snippet="Defines situation awareness and its relationship to decision making in dynamic environments.",
        abstract="Proposes a theory of situation awareness as perception, comprehension, and projection, and connects it to performance and decision quality.",
    ),

    # ---- NEW: trust / reliance / automation cluster ----
    "parasuraman_2000": Paper(
        paper_id="parasuraman_2000",
        title="A Model for Types and Levels of Human Interaction with Automation",
        authors="R. Parasuraman, T. Sheridan, C. Wickens",
        year=2000,
        venue="IEEE Transactions (Demo)",
        relevance=0.79,
        keywords=["automation", "trust", "human-AI interaction"],
        snippet="Framework for levels of automation and how they affect monitoring and reliance.",
        abstract="Presents a taxonomy of automation levels and discusses how design choices shape human monitoring, workload, and appropriate reliance.",
    ),
    "hoff_rashid_trust_2016": Paper(
        paper_id="hoff_rashid_trust_2016",
        title="Trust in Automation: Integrating Empirical Evidence Across Domains",
        authors="K. Hoff, A. Bashir",
        year=2016,
        venue="Human Factors (Demo)",
        relevance=0.73,
        keywords=["trust", "calibration", "automation"],
        snippet="Synthesizes factors influencing trust calibration including transparency and experience.",
        abstract="Reviews empirical findings on trust in automation, identifying drivers of trust, misuse/disuse, and strategies to improve calibration.",
    ),
    "calibrated_confidence_2019": Paper(
        paper_id="calibrated_confidence_2019",
        title="Communicating Model Confidence for Calibrated Reliance",
        authors="A. Park et al.",
        year=2019,
        venue="(Demo) CHI",
        relevance=0.69,
        keywords=["trust", "calibration", "transparency"],
        snippet="Studies UI confidence cues and their effect on over/under-reliance.",
        abstract="Examines how confidence displays and performance histories influence reliance, including cases where confidence can mislead when poorly calibrated.",
    ),

    # ---- NEW: interpretability / XAI evaluation cluster ----
    "xai_user_eval_2018": Paper(
        paper_id="xai_user_eval_2018",
        title="Human-Centered Evaluation of Explanations: Tasks, Measures, and Pitfalls",
        authors="V. Lai et al.",
        year=2018,
        venue="(Demo) CHI",
        relevance=0.71,
        keywords=["explainable AI", "evaluation", "human-AI interaction"],
        snippet="Compares explanation styles and measures effects on understanding and decision quality.",
        abstract="Presents a set of evaluation approaches for explanation interfaces and discusses pitfalls where explanations increase confidence without improving correctness.",
    ),
    "model_cards_2019": Paper(
        paper_id="model_cards_2019",
        title="Model Cards for Model Reporting",
        authors="M. Mitchell et al.",
        year=2019,
        venue="FAT* (Demo)",
        relevance=0.67,
        keywords=["transparency", "documentation", "human-centered AI"],
        snippet="Documentation approach to communicate intended use, limitations, and evaluation.",
        abstract="Proposes standardized documentation for models to support informed use, communicating evaluation context, performance, and limitations.",
    ),

    # ---- NEW: error boundary / predictability cluster ----
    "failure_modes_2020": Paper(
        paper_id="failure_modes_2020",
        title="Summarizing Model Failure Modes for Non-Expert Users",
        authors="J. Rivera et al.",
        year=2020,
        venue="(Demo) UIST",
        relevance=0.72,
        keywords=["error boundaries", "predictability", "human understanding"],
        snippet="Techniques to show users where a model tends to fail, supporting better mental models.",
        abstract="Explores ways to summarize failure regions and communicate them to users so they can anticipate errors and allocate attention effectively.",
    ),
    "selective_prediction_2017": Paper(
        paper_id="selective_prediction_2017",
        title="Selective Prediction: Abstention Mechanisms for Safer Human-AI Collaboration",
        authors="S. Gupta et al.",
        year=2017,
        venue="(Demo) ICML",
        relevance=0.68,
        keywords=["predictability", "human-AI teaming", "trust"],
        snippet="Abstention to avoid low-confidence errors, intended to improve collaboration safety.",
        abstract="Introduces abstention/deferral strategies that can reduce catastrophic errors, and discusses implications for user reliance and workflow design.",
    ),
}

HARDCODED_RESULTS: Dict[str, List[Paper]] = {
    SEED_TITLE: [
        PAPERS["norman_1983"],
        PAPERS["ribeiro_2016_lime"],
        PAPERS["kaur_2020_trust"],
        PAPERS["amershi_2019_collab"],
        PAPERS["lipton_2018_mythos"],
        PAPERS["bansal_2021_error"],
        PAPERS["lee_see_2004_trust"],
        PAPERS["shneiderman_2020_control"],
    ]
}

# ----------------------------
# Citation edges
# ----------------------------

CITES: Dict[str, List[str]] = {
    "seed": [p.paper_id for p in HARDCODED_RESULTS[SEED_TITLE]],

    "norman_1983": [
        "johnson_laird_1983",
        "gentner_structure_mapping_1983",
        "endsley_sa_1995",
        "klein_sensemaking_1998",
        "hutchins_cognition_1995",
    ],

    "ribeiro_2016_lime": ["doshi_velez_2017", "miller_2019_explanations", "xai_user_eval_2018"],
    "lipton_2018_mythos": ["doshi_velez_2017", "miller_2019_explanations"],
    "doshi_velez_2017": ["xai_user_eval_2018", "model_cards_2019"],
    "xai_user_eval_2018": ["model_cards_2019"],
    "model_cards_2019": [],

    "kaur_2020_trust": ["zhang_2020_calibration", "miller_2019_explanations", "calibrated_confidence_2019"],
    "lee_see_2004_trust": ["parasuraman_2000", "hoff_rashid_trust_2016"],
    "zhang_2020_calibration": ["hoff_rashid_trust_2016", "calibrated_confidence_2019"],
    "parasuraman_2000": ["hoff_rashid_trust_2016"],
    "hoff_rashid_trust_2016": ["calibrated_confidence_2019"],
    "calibrated_confidence_2019": [],

    "amershi_2019_collab": ["khanna_2022_feedback", "shneiderman_2020_control", "parasuraman_2000"],
    "khanna_2022_feedback": ["amershi_2019_collab"],

    "bansal_2021_error": ["wu_2021_error_boundary", "failure_modes_2020", "selective_prediction_2017", "yang_2023_transparency"],
    "wu_2021_error_boundary": ["failure_modes_2020", "selective_prediction_2017"],
    "failure_modes_2020": ["selective_prediction_2017"],
    "selective_prediction_2017": [],

    "shneiderman_2020_control": ["model_cards_2019", "yang_2023_transparency"],
    "yang_2023_transparency": ["calibrated_confidence_2019", "model_cards_2019"],

    "johnson_laird_1983": [],
    "gentner_structure_mapping_1983": [],
    "hutchins_cognition_1995": [],
    "klein_sensemaking_1998": [],
    "endsley_sa_1995": [],

    "miller_2019_explanations": ["johnson_laird_1983", "lee_see_2004_trust"],
}

# ----------------------------
# Keyword grouping logic
# ----------------------------

def group_non_ai(papers: List[Paper]) -> Dict[str, List[Paper]]:
    groups: Dict[str, List[Paper]] = {}
    for p in papers:
        for kw in p.keywords:
            groups.setdefault(kw, []).append(p)
    return groups

AI_CANONICAL: Dict[str, str] = {
    "mental models": "Mental Models & Interpretability",
    "human understanding": "Mental Models & Interpretability",
    "cognition": "Mental Models & Interpretability",
    "sensemaking": "Mental Models & Interpretability",
    "situation awareness": "Mental Models & Interpretability",
    "distributed cognition": "Mental Models & Interpretability",
    "reasoning": "Mental Models & Interpretability",
    "analogy": "Mental Models & Interpretability",

    "explainable AI": "Explainability & Transparency",
    "explainability": "Explainability & Transparency",
    "transparency": "Explainability & Transparency",
    "documentation": "Explainability & Transparency",
    "evaluation": "Explainability & Transparency",
    "interpretability": "Explainability & Transparency",

    "human-AI teaming": "Human–AI Collaboration",
    "human-AI interaction": "Human–AI Collaboration",
    "collaboration": "Human–AI Collaboration",
    "design patterns": "Human–AI Collaboration",
    "human-centered AI": "Human–AI Collaboration",
    "control": "Human–AI Collaboration",

    "trust": "Trust, Calibration & Reliance",
    "calibration": "Trust, Calibration & Reliance",
    "automation": "Trust, Calibration & Reliance",

    "error boundaries": "Error Predictability",
    "predictability": "Error Predictability",
}

def canonicalize_keyword(kw: str) -> str:
    return AI_CANONICAL.get(kw.strip(), kw.strip())

def group_ai(papers: List[Paper]) -> Dict[str, List[Paper]]:
    groups: Dict[str, List[Paper]] = {}
    for p in papers:
        for kw in p.keywords:
            canon = canonicalize_keyword(kw)
            groups.setdefault(canon, []).append(p)
    return groups

# ----------------------------
# Query param helpers
# ----------------------------

def get_qp() -> Dict[str, str]:
    try:
        return dict(st.query_params)
    except Exception:
        qp = st.experimental_get_query_params()
        return {k: (v[0] if isinstance(v, list) and v else v) for k, v in qp.items()}

def set_qp(**params) -> None:
    current = get_qp()
    merged = {**current, **params}
    merged = {k: v for k, v in merged.items() if v is not None}

    try:
        st.query_params.clear()
        for k, v in merged.items():
            st.query_params[k] = v
    except Exception:
        st.experimental_set_query_params(**{k: [v] for k, v in merged.items()})

    st.rerun()

# ----------------------------
# Chain-in-URL helpers (FIX)
# ----------------------------

def parse_chain(chain_str: str) -> List[str]:
    if not chain_str:
        return []
    return [x for x in chain_str.split(",") if x]

def chain_to_str(chain: List[str]) -> str:
    return ",".join(chain)

def get_chain() -> List[str]:
    qp = get_qp()
    return parse_chain(qp.get("chain", ""))

def set_chain(chain: List[str]) -> None:
    st.session_state["viewed_papers"] = chain

def start_new_chain() -> List[str]:
    return ["seed_paper"]

def append_to_chain(chain: List[str], paper_id: str) -> List[str]:
    if not chain or chain[-1] != paper_id:
        chain = chain + [paper_id]
    return chain

def goto_landing():
    set_qp(page="landing", paper=None, chain=None)

def goto_results(chain: List[str] | None = None):
    if chain is None:
        chain = get_chain()
    set_qp(page="results", paper=None, chain=chain_to_str(chain))

def goto_details(paper_id: str, chain: List[str]):
    set_qp(page="details", paper=paper_id, chain=chain_to_str(chain))

# ----------------------------
# UI helpers
# ----------------------------

def get_query_key(user_query: str) -> str:
    q = (user_query or "").strip()
    return q if q in HARDCODED_RESULTS else DEFAULT_QUERY_KEY

def cited_papers(paper_id: str) -> List[Paper]:
    ids = CITES.get(paper_id, [])
    return [PAPERS[i] for i in ids if i in PAPERS]

def inject_css() -> None:
    st.markdown(
        """
        <style>
          a.paper-card-link {
            display: block;
            color: inherit;
            text-decoration: none;
          }
          a.paper-card-link:hover .paper-card {
            border-color: rgba(49, 51, 63, 0.45);
          }
          a.paper-card-link:hover .paper-title {
            text-decoration: underline;
          }
          .paper-card {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
          }
          .paper-title {
            font-size: 1.10rem;
            font-weight: 650;
            margin-bottom: 4px;
            line-height: 1.25;
          }
          .paper-meta {
            color: rgba(49, 51, 63, 0.7);
            font-size: 0.9rem;
            margin-bottom: 8px;
          }

          .history-sidebar {
            position: sticky;
            top: 1rem;
            max-height: calc(100vh - 2rem);
            overflow-y: auto;
            padding: 1rem;
            background-color: rgba(240, 242, 246, 0.5);
            border-radius: 8px;
            border: 1px solid rgba(49, 51, 63, 0.1);
          }
          .history-item {
            padding: 0.5rem;
            margin-bottom: 0.5rem;
            background-color: white;
            border-radius: 4px;
            border: 1px solid rgba(49, 51, 63, 0.1);
            font-size: 0.85rem;
            cursor: pointer;
            transition: border-color 0.2s;
          }
          .history-item:hover { border-color: rgba(49, 51, 63, 0.3); }
          .history-item-title {
            font-weight: 600;
            margin-bottom: 0.25rem;
            line-height: 1.2;
          }
          .history-item-meta {
            color: rgba(49, 51, 63, 0.6);
            font-size: 0.75rem;
          }

       
          .landing-title{
            margin-bottom: 0.25rem;
          }
          .landing-subtitle{
            margin-top: 0;
            margin-bottom: 1.25rem;
            color: rgba(49, 51, 63, 0.75);
          }

          /* --- landing alignment wrapper --- */
.landing-wrap {
  max-width: 800px;   /* adjust: 900–1200 depending on taste */
  margin: 0 auto;      /* center wrapper */
  padding-top: 0.5rem;
}
.landing-wrap h1, .landing-wrap p {
  text-align: left;    /* keep nice left alignment */
}

        </style>
        """,
        unsafe_allow_html=True,
    )

def render_back_left(label: str, where: str) -> None:
    left, _ = st.columns([1, 9])
    with left:
        if st.button(label, use_container_width=True, key=f"back_{where}"):
            if where == "landing":
                goto_landing()
            elif where == "results":
                goto_results(get_chain())
            else:
                goto_landing()

def render_landing_search(key: str) -> str:
    with st.form(key="landing_form", clear_on_submit=False):
        q = st.text_input(
            "",
            value=st.session_state.get("query", ""),
            placeholder=f"e.g., {SEED_TITLE}",
            key=key,
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Search", type="primary", use_container_width=True)
        if submitted:
            st.session_state["query"] = q
            chain = start_new_chain()
            set_chain(chain)
            goto_results(chain)

    return st.session_state.get(key, "")



def render_results_topbar(key: str) -> str:
    """
    Results page: input on the left, Search + Back side-by-side on the right.
    Both buttons are inside the SAME form to avoid weird container behavior.
    """
    with st.form(key="results_form", clear_on_submit=False):
        c1, c2, c3 = st.columns([7.5, 1.25, 1.25], vertical_alignment="bottom")


        with c1:
            q = st.text_input(
                "Seed paper / query",
                value=st.session_state.get("query", ""),
                key=key,
                placeholder="Type a paper title, DOI, or citation…",
            )

        with c2:
            do_search = st.form_submit_button("Search", type="primary", use_container_width=True)

        with c3:
            do_back = st.form_submit_button("Back", use_container_width=True)

        if do_back:
            goto_landing()

        if do_search:
            st.session_state["query"] = q
            chain = start_new_chain()
            set_chain(chain)
            goto_results(chain)

    return st.session_state.get(key, "")


    # Put the Search button aligned on the right-ish side visually
    # (Streamlit forms can’t “share” a submit button across columns cleanly, so we do a simple approach:
    # keep it in the form above, and use a little CSS to make it look right.)
    with mid:
        st.write("")  # spacing
        st.write("")  # spacing
        st.caption(" ")  # keeps vertical alignment a bit steadier

    with right:
        st.write("")
        st.write("")
        if st.button("Back", use_container_width=True, key="results_back"):
            goto_landing()

    return st.session_state.get(key, "")


def paper_card(p: Paper) -> None:
    chain = get_chain()
    next_chain = append_to_chain(chain, p.paper_id)

    st.markdown(
        f"""
        <a class="paper-card-link" href="?page=details&paper={p.paper_id}&chain={chain_to_str(next_chain)}" target="_self">
          <div class="paper-card">
            <div class="paper-title">{p.title}</div>
            <div class="paper-meta">{p.authors} • {p.venue} • {p.year} • Relevance: {p.relevance:.2f}</div>
            <div style="margin-bottom: 8px;">{p.snippet}</div>
            <div><b>Keywords:</b> {", ".join(p.keywords)}</div>
          </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

def render_viewing_history() -> None:
    # Always render from URL chain
    chain = get_chain()
    set_chain(chain)

    st.markdown('<div class="history-sidebar">', unsafe_allow_html=True)
    st.markdown("### 📚 Viewing History")

    viewed = st.session_state.get("viewed_papers", [])

    if not viewed:
        st.caption("No papers viewed yet. Click on papers to start tracking your research path.")
    else:
        st.caption(f"{len(viewed)} step(s) in your citation chain")

        for idx in range(len(viewed) - 1, -1, -1):
            paper_id = viewed[idx]
            step_num = idx + 1

            if paper_id == "seed_paper":
                st.markdown(
                    f"""
                    <div class="history-item" style="background-color: rgba(255, 243, 205, 0.5); border-left: 3px solid #ff9800;">
                      <div style="color: #ff9800; font-size: 0.7rem; font-weight: 600; margin-bottom: 0.25rem;">STEP {step_num} • SEED</div>
                      <div class="history-item-title">🌱 {SEED_TITLE[:50]}{'...' if len(SEED_TITLE) > 50 else ''}</div>
                      <div class="history-item-meta">Starting point</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif paper_id in PAPERS:
                p = PAPERS[paper_id]
                st.markdown(
                    f"""
                    <a href="?page=details&paper={p.paper_id}&chain={chain_to_str(viewed[:idx+1])}" target="_self" style="text-decoration: none; color: inherit;">
                      <div class="history-item">
                        <div style="color: rgba(49, 51, 63, 0.5); font-size: 0.7rem; font-weight: 600; margin-bottom: 0.25rem;">STEP {step_num}</div>
                        <div class="history-item-title">{p.title[:50]}{'...' if len(p.title) > 50 else ''}</div>
                        <div class="history-item-meta">{p.authors[:25]}{'...' if len(p.authors) > 25 else ''} • {p.year}</div>
                      </div>
                    </a>
                    """,
                    unsafe_allow_html=True,
                )

        if st.button("Clear History", use_container_width=True, key="clear_history"):
            goto_results(start_new_chain())  # reset to seed-only

    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Pages
# ----------------------------

def page_landing() -> None:
    inject_css()

    left, mid, right = st.columns([1.2, 2.6, 1.2])  # tweak middle to change width
    with mid:
        st.markdown('<div class="landing-wrap">', unsafe_allow_html=True)
        st.markdown("# Citation Chaining Prototype")
        st.write("Paste a paper title, DOI, or citation to start.")
        render_landing_search(key="landing_query")
        st.markdown("</div>", unsafe_allow_html=True)


  



def page_results() -> None:
    inject_css()

    query_text = render_results_topbar(key="results_query")
    st.divider()

    main_col, history_col = st.columns([3, 1])

    with main_col:
        mode = st.toggle("AI mode (merge similar keywords)", value=False)
        st.caption("Non-AI mode groups papers by exact keywords. AI mode merges related keywords into concepts.")

        query_key = get_query_key(query_text)
        papers = HARDCODED_RESULTS.get(query_key, HARDCODED_RESULTS[DEFAULT_QUERY_KEY])
        papers_sorted = sorted(papers, key=lambda p: p.relevance, reverse=True)

        groups = group_ai(papers_sorted) if mode else group_non_ai(papers_sorted)

        def group_score(item: Tuple[str, List[Paper]]) -> float:
            _, ps = item
            return max((p.relevance for p in ps), default=0.0)

        groups_ordered = sorted(groups.items(), key=group_score, reverse=True)

        st.markdown(f"### Papers cited by: _{st.session_state.get('query', query_text) or 'your query'}_")
        st.write(f"Showing **{len(papers_sorted)}** cited papers (hardcoded demo set).")

        for group_name, group_papers in groups_ordered:
            with st.expander(f"{group_name}  •  {len(group_papers)} paper(s)", expanded=True):
                for p in sorted(group_papers, key=lambda x: x.relevance, reverse=True):
                    paper_card(p)

    with history_col:
        render_viewing_history()


def page_details(paper_id: str) -> None:
    st.set_page_config(page_title="Paper • Citation Chaining Prototype", layout="wide")
    inject_css()

    render_back_left("← Back", "results")

    if paper_id not in PAPERS:
        st.warning("Paper not found in the demo dataset.")
        return

    main_col, history_col = st.columns([3, 1])

    with main_col:
        p = PAPERS[paper_id]
        st.markdown(f"# {p.title}")
        st.caption(f"{p.authors} • {p.venue} • {p.year}")

        st.markdown("### Keywords")
        st.write(", ".join(p.keywords))

        st.markdown("### Abstract")
        st.write(p.abstract)

        st.divider()
        st.markdown("### Papers this paper cites")
        kids = cited_papers(p.paper_id)

        if not kids:
            st.info("No cited papers in the demo graph for this paper.")
        else:
            for cp in sorted(kids, key=lambda x: x.relevance, reverse=True):
                paper_card(cp)

    with history_col:
        render_viewing_history()

# ----------------------------
# Router (query param based)
# ----------------------------

def main():
    qp = get_qp()
    page = qp.get("page", "landing")
    paper = qp.get("paper")

    title = "Citation Chaining Prototype"
    if page == "results":
        title = "Results • Citation Chaining Prototype"
    elif page == "details" and paper:
        title = "Paper • Citation Chaining Prototype"

    st.set_page_config(page_title=title, layout="wide")

    if "query" not in st.session_state:
        st.session_state["query"] = ""
    if "viewed_papers" not in st.session_state:
        st.session_state["viewed_papers"] = []

    if page == "results":
        page_results()
    elif page == "details" and paper:
        page_details(paper)
    else:
        page_landing()


if __name__ == "__main__":
    main()
