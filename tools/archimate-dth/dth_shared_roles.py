"""Shared DTH roles and actors (litlfred/smart-ra#133, litlfred/dth-phc#1 §3d): elements and view for smart-ra.

Source: WHO Digital Transformation Handbooks — Primary health care: optimizing
person-centred point of service systems (ISBN 9789240093362, Section 2.2 &
Chapters 3-6 "Who should be involved?" panels, PDF 24, 30, 52, 64, 68),
Supply chain (ISBN 9789240116214), Health product catalogue (ISBN 9789240116191),
Human resources for health (dth-hrh), and Substandard and falsified medical
products (dth-sfp). Workplan: litlfred/smart-ra#133 comment 1 (shared roles and
actors across DTHs) and litlfred/dth-phc#1 section 3d / Step P5.

Models the shared digital health implementation and health-system roles and
actors used by more than one DTH as ArchiMate BusinessRoles and BusinessActors
with stable UUID5 IRIs, so DTH persona blocks and BPMN swimlanes link to one
definition in smart-ra. Also links to the shared end-user and regulatory roles
already introduced in 0.3.0-draft.2 (Health worker, Health service user,
National Regulatory Authority) and the existing 0.2.0 Stakeholders (Ministry of
Health, Health Workers, Patients).

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dth_shared_roles.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/smart-ra#dth-shared-roles"
SOURCE = "WHO Digital Transformation Handbooks (PHC 9789240093362, SC 9789240116214, PC 9789240116191, HRH, SFP); litlfred/smart-ra#133"
VIEW_FOLDER = "Primary Health Care (DTH PHC)"

RA_SKOS = "https://github.com/litlfred/smart-ra/blob/main/glossary/dpi-h-ra.glossary.json#"
PHC_SKOS = "https://github.com/litlfred/dth-phc/blob/main/glossary/dth-phc.glossary.json#"
SHARED_DTHS = "dth-phc, dth-hrh, dth-sc, dth-pc, dth-sfp"


def role_props(page, term, **kw):
    d = {
        "dthPage": f"PDF {page}",
        "skosConcept": RA_SKOS + term,
        "skosConceptPhc": PHC_SKOS + term,
        "sharedWith": SHARED_DTHS,
    }
    d.update(kw)
    return d


ELEMENTS = {
    # Shared governance & implementation actors (BusinessActor), dth-phc#1 §3d (PDF 24, 30, 52, 64, 68)
    "public-health-authority": (
        "BusinessActor",
        "Public health authority",
        "National or subnational public health authority (such as a ministry of health) responsible for governance, health and digital health policies, change management, local adoption, cybersecurity, privacy, confidentiality, data use policies, and leading scale-up and phase-out of paper or legacy systems. (Section 2.2, Ch. 3, 5 & 6 panels, PDF 24, 30, 64, 68)",
        role_props("24, 30, 64, 68", "public-health-authority", **{"fhir-actor": "PublicHealthAuthority"},
                   altLabel="Ministry of health; Subnational health authority",
                   candidateMatch="Ministry of Health (Stakeholder, id-1c5c0bc9234e4282b654dbc71b9da706)"),
    ),
    "implementing-team": (
        "BusinessActor",
        "Implementing team",
        "Multidisciplinary project and implementation team commissioning and coordinating requirements gathering, software and vendor selection, design and adaptation, end-user training, user acceptance testing, deployment, and scale-up in collaboration with the public health authority and technology partners. (Section 2.2, Ch. 3-6 panels, PDF 24, 30, 52, 64, 68)",
        role_props("24, 30, 52, 64, 68", "implementing-team", **{"fhir-actor": "ImplementingTeam"},
                   altLabel="Digital health implementation team; Project team"),
    ),
    # Shared DTH implementation & specialist roles (BusinessRole), dth-phc#1 §3d (PDF 24, 30, 52, 64, 68)
    "business-analyst": (
        "BusinessRole",
        "Business analyst",
        "Gathers and optimizes the content and functional requirements for adapting or developing a digital health solution; leads requirements gathering alongside health informaticians and user researchers, and provides continuous feedback to the engineering team during design and adaptation to ensure proper translation of requirements into implementation. (Section 2.2, Ch. 3-4 panels, PDF 24, 30, 52)",
        role_props("24, 30, 52", "business-analyst", **{"fhir-actor": "BusinessAnalyst"},
                   skosExactMatch="smart-base:SGAuthoring.Persona.BusinessAnalyst"),
    ),
    "health-informatician": (
        "BusinessRole",
        "Health informatician",
        "Leads requirements gathering alongside business analysts and user researchers, and provides expert guidance during design and adaptation to ensure the digital health system adheres to semantic classifications, terminology standards and syntactic interoperability standards such as HL7 FHIR. (Section 2.2, Ch. 3-4 panels, PDF 24, 30, 52)",
        role_props("24, 30, 52", "health-informatician", **{"fhir-actor": "HealthInformatician"}),
    ),
    "user-researcher": (
        "BusinessRole",
        "User researcher",
        "Person trained in user research who leads the process of understanding end-users, conducting contextual observations and interviews, and gathering user requirements alongside business analysts and health informaticians. (Ch. 3 panel, Sections 3.1-3.2, PDF 30-35)",
        role_props("30", "user-researcher", **{"fhir-actor": "UserResearcher"}),
    ),
    "designer": (
        "BusinessRole",
        "Designer",
        "Develops and tests prototype designs (mock-ups, wireframes, interactive prototypes) and provides continuous feedback with business analysts to the engineering team to translate user requirements into user interface design. (Section 2.2, Ch. 4 panel, Section 4.3, PDF 24, 52, 54-55)",
        role_props("24, 52", "designer", **{"fhir-actor": "Designer"},
                   altLabel="UX/UI designer; Service designer; Software designer"),
    ),
    "solutions-architect": (
        "BusinessRole",
        "Solutions architect",
        "Leads system architecture design and adaptation alongside software engineers, defining how software components, data services and interoperability standards fit within the national digital health enterprise architecture. (Ch. 4 panel, Section 4.4, PDF 52, 56-60)",
        role_props("52", "solutions-architect", **{"fhir-actor": "SolutionsArchitect"},
                   altLabel="Enterprise architect; Systems architect"),
    ),
    "software-engineer": (
        "BusinessRole",
        "Software engineer",
        "Engaged during requirements gathering to understand the operational context, leads solution design, adaptation, build and quality assurance alongside solutions architects, and incorporates end-user feedback during training, testing and roll-out. (Ch. 3-5 panels, PDF 30, 52, 64)",
        role_props("30, 52, 64", "software-engineer", **{"fhir-actor": "SoftwareEngineer"},
                   altLabel="Software developer; Developer"),
    ),
    "technology-partner": (
        "BusinessRole",
        "Technology partner",
        "Software vendor or technology partner selected to build, adapt, maintain and update the digital health solution across design, adaptation, deployment and scale-up phases in collaboration with the implementing team. (Section 2.2, Ch. 4 & 6 panels, Section 4.1, PDF 24, 52-53, 68)",
        role_props("24, 52, 68", "technology-partner", **{"fhir-actor": "TechnologyPartner"},
                   altLabel="Software vendor; Vendor; Implementer"),
    ),
    "me-specialist": (
        "BusinessRole",
        "Monitoring and evaluation specialist",
        "Determines whether the digital health system meets required performance metrics and benchmarks during scale-up so that the public health authority can safely phase out paper and/or legacy systems. (Ch. 6 panel, Section 6.3, PDF 68, 70)",
        role_props("68", "monitoring-and-evaluation-specialist", **{"fhir-actor": "MonitoringAndEvaluationSpecialist"},
                   altLabel="M&E specialist"),
    ),
}

# Reused elements from 0.2.0 and 0.3.0-draft.2 (dth_sc.py, dth_phc.py)
EXISTING = {
    "ministry-of-health": "id-1c5c0bc9234e4282b654dbc71b9da706",   # Ministry of Health (Stakeholder, 0.2.0)
    "health-workers-sh": "id-8d3dd8b68d504c2a9fe8cf414b16c127",    # Health Workers (Stakeholder, 0.2.0)
    "patients": "id-a2320dbc07e6450b94f3f0f3e03bb877",             # Patients (Stakeholder, 0.2.0)
    "nra": "id-8e67c8e9e1195cdc857b03a2c640e7fe",                  # National Regulatory Authority (BusinessRole, dth_sc.py)
    "health-worker": "id-54d7e249c99a59c6a2085f17060de254",        # Health worker (BusinessRole, dth_phc.py)
    "health-service-user": "id-0b80b004c74f5b00b4a5bc56e9c06ac0",  # Health service user (BusinessRole, dth_phc.py)
}

EXISTING_RELATIONS = {
    ("Association", "health-service-user", "patients"): "id-a17f0d5a7834524bb9be5f4b76b1f259",
}

DRAWN = [
    # Row 0-1: Governance & public health authority relationships
    ("Association", "public-health-authority", "ministry-of-health", {"name": "candidateMatch"}),
    ("Assignment", "public-health-authority", "nra"),
    ("Serving", "implementing-team", "public-health-authority"),
    ("Serving", "me-specialist", "public-health-authority"),
    # Row 0-2: Implementing team assignments to specialist roles
    ("Assignment", "implementing-team", "me-specialist"),
    ("Assignment", "implementing-team", "health-informatician"),
    ("Assignment", "implementing-team", "user-researcher"),
    ("Assignment", "implementing-team", "solutions-architect"),
    ("Assignment", "implementing-team", "business-analyst"),
    ("Assignment", "implementing-team", "designer"),
    # Row 0-3: Requirements, architecture, design & engineering collaboration
    ("Serving", "health-informatician", "solutions-architect"),
    ("Serving", "solutions-architect", "designer"),
    ("Serving", "business-analyst", "user-researcher"),
    ("Serving", "business-analyst", "designer"),
    ("Serving", "business-analyst", "software-engineer"),
    ("Serving", "designer", "software-engineer"),
    ("Aggregation", "technology-partner", "designer"),
    ("Aggregation", "technology-partner", "software-engineer"),
    # Row 1-3: End-user engagement & stakeholder links
    ("Serving", "user-researcher", "health-service-user"),
    ("Serving", "user-researcher", "health-worker"),
    ("Serving", "business-analyst", "health-worker"),
    ("Serving", "health-worker", "health-service-user"),
    ("Association", "health-service-user", "patients", {"name": "candidateMatch (dth-phc#1 §7)"}),
    ("Association", "health-worker", "health-workers-sh", {"name": "candidateMatch"}),
]

MODEL_ONLY = [
    ("Assignment", "implementing-team", "software-engineer"),
    ("Assignment", "implementing-team", "technology-partner"),
    ("Aggregation", "technology-partner", "solutions-architect"),
    ("Serving", "health-informatician", "business-analyst"),
    ("Serving", "technology-partner", "public-health-authority"),
]

_seen = set(EXISTING_RELATIONS.keys())
RELATIONS = []
for r in DRAWN + MODEL_ONLY:
    k = (r[0], r[1], r[2])
    if k not in _seen:
        _seen.add(k)
        RELATIONS.append(r)


def b(key):
    return ("box", key)


def boxes(*keys):
    return [b(k) for k in keys]


V_ROLES = "Shared DTH Roles and Actors"

VIEWS = [
    (
        V_ROLES,
        "Shared Digital Transformation Handbook (DTH) governance, implementation, specialist and end-user roles and actors (smart-ra#133 comment 1; dth-phc#1 §3d / Step P5), linking the Implementing team, Public health authority, Technology partner and specialist Business Roles (Business analyst, Health informatician, User researcher, Designer, Solutions architect, Software engineer, Monitoring and evaluation specialist, National Regulatory Authority) with end-user roles (Health worker, Health service user) and 0.2.0 Stakeholders (Ministry of Health, Health Workers, Patients).",
        (
            "col",
            [
                ("row", boxes("ministry-of-health", "public-health-authority", "me-specialist", "health-informatician")),
                ("row", boxes("nra", "user-researcher", "implementing-team", "solutions-architect")),
                ("row", boxes("health-service-user", "health-worker", "business-analyst", "designer")),
                ("row", boxes("patients", "health-workers-sh", "software-engineer", "technology-partner")),
            ],
        ),
    ),
]

VIEW_CONNECTIONS = {
    V_ROLES: DRAWN,
}
