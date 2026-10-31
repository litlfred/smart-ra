"""Primary health care DTH (litlfred/dth-phc): elements and view for smart-ra.

Source: WHO, Digital transformation handbook for primary health care:
optimizing person-centred point of service systems, 2024 (ISBN 9789240093362),
L1 entry who-iris/library/9789240093362-eng. Workplan: litlfred/dth-phc#1,
section 3c (Step P5); litlfred/smart-ra#133, task S3.

Only what the handbook states is modelled: the generic Point-of-service
application (PCPOSS) and its four specialized application types (Section 1.1,
PDF 18; Glossary, PDF 8-9), the five PCPOSS digital health intervention
services not yet in 0.2.0 (Section 1.1, PDF 18), the end-user roles Health
worker and Health service user (with candidateMatch to the existing 0.2.0
Stakeholder "Patients", per dth-phc#1 sections 3c and 7), and the reused 0.2.0
components they connect to (Section 1.1, Fig. 4, Section 4.4, PDF 18-19, 56-60).

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dth_phc.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/dth-phc#archimate"
SOURCE = "WHO Digital transformation handbook for primary health care: optimizing person-centred point of service systems (9789240093362); litlfred/dth-phc"
VIEW_FOLDER = "Primary Health Care (DTH PHC)"

SKOS = "https://github.com/litlfred/dth-phc/blob/main/glossary/dth-phc.glossary.json#"
RA_SKOS = "https://github.com/litlfred/smart-ra/blob/main/glossary/dpi-h-ra.glossary.json#"


def p(page, term=None, **kw):
    d = {"dthPage": f"PDF {page}", **kw}
    if term:
        d["skosConcept"] = SKOS + term
    return d


ELEMENTS = {
    # Point-of-service application (generic) and its four specializations, Section 1.1 (PDF 18) & Glossary (PDF 8-9)
    "pos-app": (
        "ApplicationComponent",
        "Point-of-service application",
        "Person-centred point of service system (PCPOSS) are digital systems that facilitate the provision and delivery of health services to individuals (i.e. persons, clients, patients, health service users) at the point of service or point of care. This includes software capabilities and embedded health interoperability standards that enable health workers to access, record and update individuals' health information, and to screen, manage, treat, and/or communicate with individuals. PCPOSS encompass community-based information systems, decision support systems, electronic health record systems and personal health records. (PDF 9, 18)",
        p(18, "person-centred-point-of-service-system",
          altLabel="PCPOSS",
          skosBroader=RA_SKOS + "point-of-service-applications"),
    ),
    "ehr-system": (
        "ApplicationComponent",
        "Electronic health record system",
        "A secure, online system that holds health service user health records, which include information about people's health and clinical care. This system is managed by health workers. Also referred to as an 'electronic medical record system'. (PDF 8, 18)",
        p(18, "electronic-health-record-system",
          altLabel="EHR system",
          skosConceptRa=RA_SKOS + "point-of-service-applications"),
    ),
    "dss": (
        "ApplicationComponent",
        "Decision support system",
        "A digital job aid that combines an individual's health information with the health worker's knowledge and clinical protocols, to assist health workers in making diagnosis and treatment decisions. (PDF 8, 18)",
        p(18, "decision-support-system",
          altLabel="DSS",
          candidateMatch="Decision Support Engine (id-539b04ae45f147258d8253ae5cb87402)"),
    ),
    "chis": (
        "ApplicationComponent",
        "Community-based information system",
        "Applications that facilitate data collection and use at the community level. These applications are utilized by community-based workers who provide health promotion and disease prevention activities. (PDF 8, 18)",
        p(18, "community-based-information-system",
          altLabel="CHIS"),
    ),
    "phr": (
        "ApplicationComponent",
        "Personal health record",
        "A record of an individual's health information in a structured digital format for a set of defined use cases over which the person has agency. (PDF 18)",
        p(18, "personal-health-record",
          altLabel="PHR"),
    ),
    # Business roles at the point of service, Section 1.1 (PDF 18-19) & Glossary (PDF 9)
    "health-worker": (
        "BusinessRole",
        "Health worker",
        "End-users of a PCPOSS at the point of care (point of service), including all health worker occupational groups operating at all care levels and outside of formal health-care facilities (e.g. community health workers and health volunteers). (PDF 19)",
        p(19, "health-worker",
          candidateMatch="Health Workers (Stakeholder, id-8d3dd8b68d504c2a9fe8cf414b16c127)"),
    ),
    "health-service-user": (
        "BusinessRole",
        "Health service user",
        "Also known as patients, clients or beneficiaries, these are individuals who receive formal and/or informal health services. (PDF 9, 18)",
        p(9, "health-service-users",
          altLabel="Health service users; Patient; Client; Beneficiary",
          candidateMatch="Patients (Stakeholder, id-a2320dbc07e6450b94f3f0f3e03bb877); Individual (BusinessRole, id-03e28af10b8f5b099e271461c8a99f21)"),
    ),
    # Application services for the PCPOSS DHIs not yet in 0.2.0, Section 1.1 (PDF 18)
    "alerts-and-reminders": (
        "ApplicationService",
        "Alerts and reminders",
        "DHI 1.1.3 Transmit targeted alerts and reminders to health service user(s); DHI 2.3.1 Provide prompts and alerts according to protocols. (PDF 18)",
        p(18, dhiCode="1.1.3; 2.3.1"),
    ),
    "longitudinal-tracking": (
        "ApplicationService",
        "Longitudinal tracking",
        "DHI 2.2.1 Longitudinal tracking of a health service user's health status and services: ongoing and systematic collection and analysis of data related to a health service user's health status, treatment and outcomes over multiple encounters or visits. (PDF 9, 18)",
        p(18, "longitudinal-tracking", dhiCode="2.2.1"),
    ),
    "care-checklists": (
        "ApplicationService",
        "Care checklists",
        "DHI 2.3.2 Provide checklists according to protocols. (PDF 18)",
        p(18, altLabel="Checklists", dhiCode="2.3.2"),
    ),
    "clinical-screening": (
        "ApplicationService",
        "Clinical screening",
        "DHI 2.3.3 Screen persons by risk or other health status; DHI 2.7.1 Identify persons in need of services. (PDF 18)",
        p(18, altLabel="Screening", dhiCode="2.3.3; 2.7.1"),
    ),
    "indicator-reporting": (
        "ApplicationService",
        "Indicator reporting",
        "DHI 2.2.4 Routine health indicator data collection and management; DHI 4.1.2 Data storage and aggregation; DHI 4.1.3 Data synthesis and visualizations. Collect primary data once at the point of care to calculate aggregate indicators for reporting and accountability (Fig. 4, PDF 18-19).",
        p(18, dhiCode="2.2.4; 4.1.2; 4.1.3"),
    ),
}

EXISTING = {
    "patients": "id-a2320dbc07e6450b94f3f0f3e03bb877",             # Patients (Stakeholder; dth-phc#1 §3c/§7: Health service user)
    "shr": "id-f180ad44b2e94e2a9ee8523ffc900264",                  # Shared Health Record (BusinessObject, SHR view)
    "shr-repo": "id-0e6d89398fff4f20994a31b4de58e7d7",             # SHR Repository (ApplicationComponent, SHR view)
    "dse": "id-539b04ae45f147258d8253ae5cb87402",                  # Decision Support Engine (ApplicationComponent, CDS view)
    "terminology-service": "id-3f41de2b51c24041b08243bf72b140d1",  # Terminology Service (ApplicationComponent)
    "limr": "id-c0d39bf67fe64f54b07fbeb9bf37d404",                 # Logical Information Model Registry (ApplicationComponent)
    "hwr": "id-350840520ae44f658b6ad3b3762e382e",                  # DPI-H Health Workforce Registry (HWR) (ApplicationComponent)
    "facility-registry": "id-5f6d9b9678824b37b95952735420ae8d",    # Facility registry (ApplicationComponent)
    "analytics-platform": "id-3fd92d497ca040c8a436f355c0b68770",   # Analytics & Reporting Platform (ApplicationComponent)
    "client-identity": "id-788f660553e14f0283b93c2dda3ae441",      # Client Identity Management (Capability)
    "interop-component": "id-80856538cbd44167a37b276e38c994c3",    # Interoperability Component (ApplicationComponent)
}

DHI_SERVICES = [
    "alerts-and-reminders",
    "longitudinal-tracking",
    "care-checklists",
    "clinical-screening",
    "indicator-reporting",
]
POS_TYPES = ["phr", "ehr-system", "dss", "chis"]

# Relationships stated by the handbook (Section 1.1, Fig. 4, Section 4.4)
SPECIALIZATIONS = [("Specialization", t, "pos-app") for t in POS_TYPES]
REALIZATIONS = [("Realization", "pos-app", s) for s in DHI_SERVICES]

DRAWN = [
    # End-users & services in rows 0-1
    ("Association", "health-service-user", "patients", {"name": "candidateMatch (dth-phc#1 §7)"}),
    ("Serving", "alerts-and-reminders", "health-service-user"),
    ("Serving", "alerts-and-reminders", "health-worker"),
    ("Serving", "longitudinal-tracking", "health-worker"),
    ("Serving", "dss", "health-worker"),
    ("Realization", "dss", "care-checklists"),
    ("Realization", "dss", "clinical-screening"),
    ("Serving", "dse", "dss"),
    # PCPOSS core hub in row 2 and its immediate Moore neighbors in rows 1-3
    ("Realization", "pos-app", "alerts-and-reminders"),
    ("Realization", "pos-app", "longitudinal-tracking"),
    ("Specialization", "dss", "pos-app"),
    ("Specialization", "ehr-system", "pos-app"),
    ("Realization", "pos-app", "indicator-reporting"),
    ("Specialization", "phr", "pos-app"),
    ("Flow", "pos-app", "interop-component"),
    ("Specialization", "chis", "pos-app"),
    # Records, identity & reporting in rows 1-3
    ("Access", "ehr-system", "shr", {"accessType": 3}),
    ("Realization", "ehr-system", "client-identity"),
    ("Realization", "interop-component", "client-identity"),
    ("Flow", "indicator-reporting", "analytics-platform"),
    # Interoperability & foundational DPI-H services in rows 3-4
    ("Flow", "interop-component", "shr-repo"),
    ("Serving", "hwr", "interop-component"),
    ("Serving", "terminology-service", "interop-component"),
    ("Serving", "limr", "interop-component"),
    ("Serving", "facility-registry", "chis"),
]

MODEL_ONLY = [
    ("Realization", "pos-app", "care-checklists"),
    ("Realization", "pos-app", "clinical-screening"),
    ("Serving", "pos-app", "health-worker"),
    ("Serving", "pos-app", "health-service-user"),
    ("Serving", "phr", "health-service-user"),
    ("Serving", "chis", "health-worker"),
    ("Realization", "ehr-system", "longitudinal-tracking"),
    ("Realization", "pos-app", "client-identity"),
    ("Access", "pos-app", "shr", {"accessType": 3}),
    ("Flow", "interop-component", "analytics-platform"),
]

_seen = set()
RELATIONS = []
for r in DRAWN + SPECIALIZATIONS + REALIZATIONS + MODEL_ONLY:
    k = (r[0], r[1], r[2])
    if k not in _seen:
        _seen.add(k)
        RELATIONS.append(r)


def b(key):
    return ("box", key)


def boxes(*keys):
    return [b(k) for k in keys]


V_PCPOSS = "Person-centred point of service (PCPOSS)"

VIEWS = [
    (
        V_PCPOSS,
        "Person-centred point of service system (PCPOSS) and its four specialized application types (electronic health record system, decision support system, community-based information system, personal health record), the five PCPOSS digital health intervention services (Section 1.1, PDF 18), end-user roles (Health worker and Health service user / Patients), and interoperability with foundational DPI-H registries, repositories, terminology, clinical decision support and analytics (Fig. 4, Section 4.4, PDF 18-19, 56-60).",
        (
            "col",
            [
                ("row", boxes("patients", "health-service-user", "health-worker", "care-checklists", "clinical-screening")),
                ("row", boxes("shr", "alerts-and-reminders", "longitudinal-tracking", "dss", "dse")),
                ("row", boxes("client-identity", "ehr-system", "pos-app", "indicator-reporting", "analytics-platform")),
                ("row", boxes("shr-repo", "interop-component", "phr", "chis")),
                ("row", boxes("hwr", "terminology-service", "limr", "facility-registry")),
            ],
        ),
    ),
]

VIEW_CONNECTIONS = {
    V_PCPOSS: DRAWN,
}
