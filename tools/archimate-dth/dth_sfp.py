"""Substandard and falsified medical products DTH (litlfred/dth-sfp): elements and views for smart-ra.

Source: WHO, Digital transformation handbook for reporting substandard and
falsified medical products, 2026 (ISBN 9789240120747, IRIS 187cabc7), L1 entry
who-iris/library/9789240120747-eng. Workplan: litlfred/dth-sfp#1, §2.2, §2.3,
§2.4 and Step P3; litlfred/smart-ra#133.

Only what the handbook states is modelled. Shared elements from 0.2.0 and from
the Supply Chain (dth_sc.py), Product Catalogue (dth_pc.py), Primary Health Care
(dth_phc.py), and Shared Roles (dth_shared_roles.py) specifications are reused
by id and never redefined.

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dth_sfp.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/dth-sfp#archimate"
SOURCE = "WHO Digital transformation handbook for reporting substandard and falsified medical products (9789240120747); litlfred/dth-sfp"
VIEW_FOLDER = "Substandard and Falsified Products (DTH SFP)"

RA_SKOS = "https://github.com/litlfred/smart-ra/blob/main/glossary/dpi-h-ra.glossary.json#"
SFP_SKOS = "https://github.com/litlfred/dth-sfp/blob/main/glossary/dth-sfp.glossary.json#"


def p(page, term=None, **kw):
    d = {"dthPage": f"PDF {page}", **kw}
    if term:
        d["skosConcept"] = SFP_SKOS + term
    return d


ELEMENTS = {
    # Motivation layer — Stakeholders (Ch. 1 §1.1, Ch. 2 §2.2–2.3, Table 1, Annex 4; PDF 15, 20, 28, 68)
    "law-enforcement-customs": (
        "Stakeholder",
        "Law Enforcement and Customs",
        "Customs officers and law enforcement agencies with whom policies are aligned to enable swift data sharing and who spearhead investigations and border control where criminal activity is suspected. (Intro p. 1, Section 2.1-2.2, PDF 13, 27-28)",
        p("13, 27-28", "law-enforcement-and-customs"),
    ),
    "health-financing-procurement": (
        "Stakeholder",
        "Health Financing and Procurement Agencies",
        "Procurement bodies, funding organizations and health insurance systems with whom policies are coordinated to detect falsified products within supply chains or reimbursement claims. (Section 1.1, Section 2.2, PDF 20, 28)",
        p(
            "20, 28",
            "health-financing-and-procurement-agencies",
            candidateMatch="Procurer (BusinessRole, id-2bfebc1bb917583cbc21e7d1bfac3164)",
        ),
    ),
    "ict-ministry": (
        "Stakeholder",
        "ICT Ministry",
        "Digital innovation and ICT ministries and agencies that collaborate to integrate the reporting system with existing national eHealth strategies or digital infrastructure. (Section 2.2, PDF 28)",
        p(28, "ict-ministry", altLabel="Innovation and ICT ministries"),
    ),
    "regional-global-regulators": (
        "Stakeholder",
        "Regional and Global Regulators",
        "Regional and global regulatory authorities (such as the European Medicines Agency, African Medicines Agency, and WHO) working to harmonize regulations, coordinate alerts, and support national authorities. (Section 2.2, PDF 28)",
        p(28, "regional-and-global-regulators", altLabel="Regional and global regulatory authorities"),
    ),
    "medical-product-industry": (
        "Stakeholder",
        "Medical Product Industry",
        "Pharmaceutical manufacturers, distributors, suppliers, and industry associations engaged in product verification, recalls, and stakeholder consultations. (Section 1.1, Section 2.3, Annex 4, PDF 20, 28, 68)",
        p(
            "20, 28, 68",
            "medical-product-industry",
            candidateMatch="Manufacturer / Distributor (BusinessRole, id-66d0f91175c154b48413d57e9f952a34)",
        ),
    ),
    "professional-associations": (
        "Stakeholder",
        "Professional Associations",
        "Health care professional associations engaged in stakeholder consultations, governance advisory councils, and mobilization to support reporting of substandard and falsified medical products. (Section 1.1, Section 2.3, Table 1, PDF 15, 20, 28)",
        p("15, 20, 28", "professional-associations", altLabel="Health care professional associations"),
    ),
    # Motivation layer — Drivers & Goals (Ch. 2 §2.4, Intro p. 1; PDF 13, 28-29)
    "driver-patient-safety": (
        "Driver",
        "Patient Safety",
        "Strategic driver to safeguard the quality of medicines, prevent adverse effects or therapeutic failure, and protect public health. (Intro p. 1, Section 2.4, PDF 13, 28-29)",
        p("13, 28-29", "patient-safety"),
    ),
    "goal-timely-regulatory-action": (
        "Goal",
        "Timely Regulatory Action",
        "Strategic goal to strengthen regulatory action on suspected substandard and falsified medical products through timely investigation, removal from the supply chain, recalls, and sanctions. (Intro p. 1, Section 2.1, Section 2.4, PDF 13, 27-28)",
        p("13, 27-28", "timely-regulatory-action"),
    ),
    "goal-supply-chain-transparency": (
        "Goal",
        "Supply Chain Transparency",
        "Strategic goal to improve supply chain transparency and reduce the prevalence of substandard and falsified medical products entering the market. (Intro p. 1, Section 2.4, PDF 13, 28)",
        p("13, 28", "supply-chain-transparency"),
    ),
    "goal-reduced-detection-to-notification-time": (
        "Goal",
        "Reduced Detection-to-Notification Time",
        "Strategic goal to reduce the average detection-to-notification time for suspected substandard and falsified medical products. (Section 2.4, PDF 28)",
        p(28, "reduced-detection-to-notification-time"),
    ),
    # Motivation layer — Assessments (Table 5 barrier categories & Annex 6; PDF 25, 70)
    "assessment-awareness-knowledge-barriers": (
        "Assessment",
        "Awareness and Knowledge Barriers",
        "Lack of awareness of substandard and falsified medical products and lack of knowledge on how to recognize and report them, addressed by integrating detection and reporting guidance within the reporting application. (Table 5, Annex 6, PDF 25, 70)",
        p("25, 70", "awareness-and-knowledge-barriers", altLabel="Education and knowledge barriers"),
    ),
    "assessment-process-operational-barriers": (
        "Assessment",
        "Process and Operational Barriers",
        "Health care professional workload and time constraints, under-resourced NMRAs, lack of trained personnel, polypharmacy, and lack of continuity of care. (Table 5, Annex 6, PDF 25, 70)",
        p(
            "25, 70",
            "process-and-operational-barriers",
            altLabel="Health care professional capacity, regulatory support, and health care system practice barriers",
        ),
    ),
    "assessment-technical-infrastructure-barriers": (
        "Assessment",
        "Technical and Infrastructure Barriers",
        "Lack of digitalization (lengthy or paper-based reporting systems) and lack of or limited internet connectivity and infrastructure in remote areas, addressed by intuitive automated reporting and offline reporting with synchronization. (Table 5, Annex 6, PDF 25, 70)",
        p("25, 70", "technical-and-infrastructure-barriers", altLabel="Technology barriers"),
    ),
    "assessment-trust-incentives-barriers": (
        "Assessment",
        "Trust and Incentives Barriers",
        "Fear of reputational, professional, personal or legal repercussions, lack of NMRA feedback, and economic or reputational damage from recalls, addressed by anonymous reporting options, reporter identity protection, legal protections, and feedback loops. (Table 5, Annex 6, PDF 25, 70)",
        p("25, 70", "trust-and-incentives-barriers", altLabel="Economic and social barriers"),
    ),
    # Strategy layer — Capabilities (Glossary p. viii, Intro p. 1, Ch. 2–4; PDF 10, 13, 22, 27, 31-43)
    "cap-post-market-surveillance": (
        "Capability",
        "Post-Market Surveillance",
        "The practice of monitoring the safety and quality of a pharmaceutical drug or medical device after it has been released on the market, including risk-based post-market surveillance (Rb-PMS) to prioritize and allocate resources by risk. (Glossary p. viii, Intro p. 1, PDF 10, 13)",
        p("10, 13", "post-market-surveillance", altLabel="PMS; Risk-based post-market surveillance (Rb-PMS)"),
    ),
    "cap-pharmacovigilance": (
        "Capability",
        "Pharmacovigilance",
        "The science and activities relating to the detection, assessment, understanding and prevention of adverse effects or any other medicine/vaccine-related problem, encompassing active and passive pharmacovigilance. (Glossary p. viii, Section 1.3, Section 2.1, PDF 10, 22, 27)",
        p("10, 22, 27", "pharmacovigilance"),
    ),
    "cap-sf-case-reporting": (
        "Capability",
        "SF Case Reporting",
        "Capability enabling health care professionals and other reporters to promptly identify, document, and submit reports of suspected substandard and falsified medical products to regulatory authorities. (Intro p. 1-2, Ch. 3-4, PDF 13-14, 31-43)",
        p("13-14, 31-43", "sf-case-reporting"),
    ),
    "cap-sf-case-investigation": (
        "Capability",
        "SF Case Investigation",
        "Capability of national medicines regulatory authorities (NMRAs) to triage, verify, and thoroughly investigate reported suspected substandard and falsified medical products, in collaboration with laboratories and law enforcement where needed. (Intro p. 1, Section 2.1, Table 9, PDF 13, 27, 39-40)",
        p("13, 27, 39-40", "sf-case-investigation"),
    ),
    "cap-regulatory-enforcement": (
        "Capability",
        "Regulatory Enforcement",
        "Capability of regulatory authorities to act on confirmed substandard and falsified medical product reports by removing products from the supply chain and market, initiating withdrawals or recalls, imposing sanctions, and issuing safety alerts. (Intro p. 1, Section 2.1, PDF 13, 27)",
        p("13, 27", "regulatory-enforcement"),
    ),
    # Business layer — Roles (Glossary p. viii, Ch. 2 §2.3, Ch. 4 §4.1, Tables 7-9; PDF 10, 15, 28, 35-41)
    "hcp-reporter": (
        "BusinessRole",
        "Health Care Professional (Reporter)",
        "An individual who provides health care treatment and advice based on formal training and experience (such as doctors, nurses, midwives, pharmacists, community health workers, laboratory technicians, paramedics, and veterinarians) who detects and reports suspected substandard and falsified medical products. (Glossary p. viii, Section 4.1, Tables 7-9, Annex 2, PDF 10, 35-41, 64)",
        p(
            "10, 35-41, 64",
            "health-care-professional-reporter",
            altLabel="Reporter; Health care professional",
            **{"fhir-actor": "HealthCareProfessionalReporter"},
            candidateMatch="Health worker (BusinessRole, id-54d7e249c99a59c6a2085f17060de254); Health Workers (Stakeholder, id-8d3dd8b68d504c2a9fe8cf414b16c127)",
        ),
    ),
    "nmra-reviewer": (
        "BusinessRole",
        "NMRA Reviewer",
        "Regulatory staff and pharmacovigilance/monitoring teams within the National Medicines Regulatory Authority who receive, review, triage, investigate, and follow up on submitted substandard and falsified medical product reports. (Table 1, Section 2.1, Table 9, Ch. 7, PDF 15, 27, 39-40, 59)",
        p("15, 27, 39-40, 59", "nmra-reviewer", altLabel="Regulatory staff; Regulatory/monitoring/pharmacovigilance teams", **{"fhir-actor": "NMRAReviewer"}),
    ),
    "steering-committee": (
        "BusinessRole",
        "Steering Committee",
        "National steering committee led by the ministry of health or NMRA that provides strategic oversight, ensures alignment with national health goals, mobilizes resources, and makes key strategic decisions on substandard and falsified medical products reporting. (Section 2.3, PDF 28)",
        p(28, "steering-committee", altLabel="National steering committee", **{"fhir-actor": "SteeringCommittee"}),
    ),
    "technical-working-group": (
        "BusinessRole",
        "Technical Working Group",
        "Multidisciplinary group of subject matter experts (medical product regulators, IT specialists, pharmacovigilance experts) working under the leadership of the steering committee, responsible for design, planning, and implementation details. (Section 2.3, PDF 28)",
        p(28, "technical-working-group", altLabel="TWG", **{"fhir-actor": "TechnicalWorkingGroup"}),
    ),
    "advisory-council": (
        "BusinessRole",
        "Advisory Council",
        "External experts, professional associations, patient advocacy groups, and private sector partners offering insights on best practices, user expectations, and emerging technologies to the steering committee and technical working group without decision-making authority. (Section 2.3, PDF 28)",
        p(28, "advisory-council", **{"fhir-actor": "AdvisoryCouncil"}),
    ),
    "project-champion": (
        "BusinessRole",
        "Project Champion",
        "High-level official or recognized expert who advocates for the project across government and partners, engages professional associations, civil society, and private sector players, and mobilizes stakeholders to obtain buy-in and address policy barriers. (Section 2.3, PDF 28)",
        p(28, "project-champion", **{"fhir-actor": "ProjectChampion"}),
    ),
    "digital-health-coordinator": (
        "BusinessRole",
        "Digital Health Coordinator",
        "Project manager or digital health coordinator responsible for overseeing daily implementation tasks, engaging key stakeholders, ensuring alignment with the national architectural blueprint and roadmap, and facilitating partnerships and user feedback loops. (Section 2.3, PDF 28)",
        p(28, "digital-health-coordinator", altLabel="Digital health coordinator / project manager", **{"fhir-actor": "DigitalHealthCoordinator"}),
    ),
    # Business layer — BusinessProcesses (Table 10, Fig. 4, Table 9, Intro p. 1, §2.1-2.2, §2.4; PDF 13, 27-28, 39-43)
    "sf-rep-001": (
        "BusinessProcess",
        "Report Suspected SF Product (SF-REP-001)",
        "Enable health care professionals to promptly identify anomalies, isolate the suspect product, capture product, batch, expiry, photo, and incident details (online or offline with synchronization), and submit a suspected substandard or falsified medical product report to the NMRA. (Table 10, Fig. 4, Table 9, Table 12, PDF 39-43)",
        p("39-43", "sf-rep-001", processId="SF-REP-001"),
    ),
    "sf-rep-002": (
        "BusinessProcess",
        "Verify Product Identity and Batch (SF-REP-002)",
        "Search the product catalogue/registry to select the product and automatically assign product type, capture or scan batch number and expiry date, and verify product details and registration status. (Table 9, Table 10, Fig. 4, Table 11-12, PDF 39-43)",
        p("39-43", "sf-rep-002", processId="SF-REP-002"),
    ),
    "sf-rep-003": (
        "BusinessProcess",
        "Triage and Route SF Report (SF-REP-003)",
        "Receive the submitted report at the NMRA, issue a confirmation and tracking number to the reporter, assess whether the report indicates substandard/falsified quality defects and/or adverse drug reactions (DE8, DE9), and route to NMRA reviewers and pharmacovigilance workflows. (Section 1.3, Section 2.1, Table 9, Fig. 4, Table 11, PDF 22, 27, 39-43)",
        p("22, 27, 39-43", "sf-rep-003", processId="SF-REP-003"),
    ),
    "sf-rep-004": (
        "BusinessProcess",
        "Investigate SF Report (SF-REP-004)",
        "Conduct regulatory and laboratory investigation of the suspected substandard or falsified medical product, following up with the reporter for additional details or retained samples and collaborating with law enforcement and customs where criminal activity is suspected. (Intro p. 1, Section 2.1-2.2, Table 9, Ch. 7, PDF 13, 27-28, 39-40, 59)",
        p("13, 27-28, 39-40, 59", "sf-rep-004", processId="SF-REP-004"),
    ),
    "sf-rep-005": (
        "BusinessProcess",
        "Take Regulatory Action and Issue Alert (SF-REP-005)",
        "Upon confirmation of a substandard or falsified medical product, remove the product from the supply chain and market, initiate product recalls or withdrawals, impose sanctions, refer criminal cases to law enforcement, and issue medical product safety alerts. (Intro p. 1, Section 2.1-2.2, Table 9, Ch. 7, PDF 13, 27-28, 39-40, 59)",
        p("13, 27-28, 39-40, 59", "sf-rep-005", processId="SF-REP-005"),
    ),
    "sf-rep-006": (
        "BusinessProcess",
        "Give Feedback to Reporter and Report to GSMS (SF-REP-006)",
        "Provide status updates, investigation outcomes, and safety alerts back to the reporting health care professional (reporter feedback loop) and submit confirmed or validated case reports to the WHO Global Surveillance and Monitoring System (GSMS) and global pharmacovigilance databases. (Intro p. 1, Table 4, Table 6, Table 9-10, Ch. 7, PDF 13, 24, 31-32, 39-41, 59)",
        p("13, 24, 31-32, 39-41, 59", "sf-rep-006", processId="SF-REP-006"),
    ),
    # Business layer — BusinessObjects (Intro p. 1-2, Table 4, Table 6, Table 9-11, Ch. 7; PDF 13-14, 24, 32, 39-43, 59)
    "bo-sf-report": (
        "BusinessObject",
        "SF Report",
        "A report of a suspected substandard or falsified medical product submitted by a health care professional or other reporter to the National Medicines Regulatory Authority, carrying product identification, batch/expiry, incident description, photos, and tracking status. (Intro p. 1-2, Table 4, Table 9-11, PDF 13-14, 24, 39-43)",
        p("13-14, 24, 39-43", "sf-report", altLabel="Substandard and falsified medical product report", **{
            "logical-model": "SFReport",
            "attribute:productIdentification": "Identifier (GTIN / Product ID)",
            "attribute:batchNumber": "string",
            "attribute:expiryDate": "date",
            "attribute:incidentDescription": "string",
            "attribute:photos": "Attachment 0..*",
            "attribute:trackingStatus": "code",
        }),
    ),
    "bo-medical-product-alert": (
        "BusinessObject",
        "Medical Product Alert",
        "Official notification or alert issued by the NMRA or WHO on confirmed or suspected substandard and falsified medical products to inform health care professionals, supply chain actors, and the public. (Table 6, Table 9, Ch. 7, PDF 32, 39-40, 59)",
        p("32, 39-40, 59", "medical-product-alert", altLabel="Safety alert; NMRA and WHO medical product alert", **{
            "logical-model": "MedicalProductAlert",
            "attribute:alertIdentifier": "Identifier",
            "attribute:issuingAuthority": "Reference(Organization) (NMRA / WHO)",
            "attribute:affectedProduct": "Reference(TradeItem)",
            "attribute:batchNumbers": "string 0..*",
            "attribute:recommendedAction": "string",
        }),
    ),
    # Application & Data layer — ApplicationComponents & DataObject (Ch. 1 §1.3, Table 4, Ch. 3 §3.2, Fig. 3, Ch. 4 §4.4, Table 11, Ch. 7)
    "sf-reporting-app": (
        "ApplicationComponent",
        "SF Reporting Application",
        "Point-of-service digital application (such as a mobile smartphone app or web form) used by health care professionals to capture and submit reports of suspected substandard and falsified medical products, receive tracking updates and alerts, and store reports offline for synchronization. (Intro p. 2, Section 3.2, Fig. 3, Ch. 4, Ch. 7, PDF 14, 33-34, 35-47, 59)",
        p(
            "14, 33-34, 35-47, 59",
            "sf-reporting-application",
            altLabel="Substandard and falsified reporting application",
            skosBroader=RA_SKOS + "point-of-service-applications",
            **{"fhir-actor": "SFReportingApplication"},
        ),
    ),
    "nmra-case-mgmt-backend": (
        "ApplicationComponent",
        "NMRA Case Management Back End",
        "Back-end regulatory information system used by the National Medicines Regulatory Authority to receive, store, triage, assign, track, and manage substandard and falsified medical product reports, initiate feedback to reporters, and exchange data with national registries and global surveillance systems. (Section 1.3, Table 4, Table 6, Table 13, Ch. 7, PDF 22, 24, 31-32, 47, 59)",
        p(
            "22, 24, 31-32, 47, 59",
            "nmra-case-management-back-end",
            sharedWith="dth-sc Regulatory Systems (id-22eff58eae365a4f8d0e0368d8c3497e)",
            **{"fhir-actor": "NMRACaseManagementBackEnd"},
        ),
    ),
    "pv-system": (
        "ApplicationComponent",
        "Pharmacovigilance System",
        "National pharmacovigilance information system and database used for collecting, recording, analysing, and evaluating adverse drug reaction (ADR) and medicine safety reports and integrating with substandard and falsified medical product reporting. (Section 1.3, Table 4, Section 2.1, Annex 5, PDF 22, 24, 27, 69)",
        p(
            "22, 24, 27, 69",
            "pharmacovigilance-system",
            sharedWith="dth-sc Regulatory Systems (id-22eff58eae365a4f8d0e0368d8c3497e)",
            **{"fhir-actor": "PharmacovigilanceSystem"},
        ),
    ),
    "who-gsms": (
        "ApplicationComponent",
        "WHO GSMS",
        "WHO Global Surveillance and Monitoring System (GSMS), WHO's global case reporting database and surveillance system to which NMRAs report data on suspected and confirmed substandard and falsified medical products to facilitate global coordination and alerts. (Abbreviations p. vi, Intro p. 1, Table 4, PDF 8, 13, 24)",
        p("8, 13, 24", "who-gsms", altLabel="WHO Global Surveillance and Monitoring System", **{"fhir-actor": "WHOGSMS"}),
    ),
    "vigiflow-vigibase": (
        "ApplicationComponent",
        "VigiFlow / VigiBase",
        "Global pharmacovigilance data management and adverse drug reaction database systems into which national pharmacovigilance centres submit satisfactory adverse drug reaction reports. (Table 4, PDF 24)",
        p(24, "vigiflow-vigibase", altLabel="Vigilance hub, VigiFlow and VigiBase", **{"fhir-actor": "VigiFlowVigiBase"}),
    ),
    "who-medical-product-alert-system": (
        "ApplicationComponent",
        "WHO Medical Product Alert System",
        "WHO global medical product alert publication system and portal providing rapid alerts on confirmed substandard and falsified medical products, linked directly from reporting applications. (Ch. 7, PDF 59)",
        p(59, "who-medical-product-alert-system", altLabel="WHO Medical Product Alert webpage", **{"fhir-actor": "WHOMedicalProductAlertSystem"}),
    ),
    "do-sf-report": (
        "DataObject",
        "SF Report Data Object",
        "Structured data record for a substandard and falsified medical product report, comprising the core data elements of Table 11 (SFR.A1.DE1 Region, DE2 Type of report, DE3 Product ID, DE4 Product description, DE5 Type of product, DE6 Batch number, DE7 Expiry date, DE8 Substandard or falsified?, DE9 Adverse reaction or lack of efficacy?, DE10 Reporting reason/description) encoded with HL7 FHIR and standard terminologies (ICD-11, SNOMED GPS). (Section 4.4, Table 11, Table 13, PDF 42-43, 47)",
        p("42-43, 47", "sf-report-data-object", **{
            "logical-model": "SFR.A1.DE1..DE10",
            "attribute:SFR.A1.DE1": "CodeableConcept 1..1 (Region)",
            "attribute:SFR.A1.DE2": "code 1..1 (Type of report)",
            "attribute:SFR.A1.DE3": "Identifier 1..1 (Product ID)",
            "attribute:SFR.A1.DE4": "string 0..1 (Product description)",
            "attribute:SFR.A1.DE5": "CodeableConcept 1..1 (Type of product)",
            "attribute:SFR.A1.DE6": "string 1..1 (Batch number)",
            "attribute:SFR.A1.DE7": "date 1..1 (Expiry date)",
            "attribute:SFR.A1.DE8": "CodeableConcept 1..1 (Substandard or falsified?)",
            "attribute:SFR.A1.DE9": "boolean 1..1 (Adverse reaction or lack of efficacy?)",
            "attribute:SFR.A1.DE10": "string 1..1 (Reporting reason / description)",
        }),
    ),
}

# Reused elements from 0.2.0 and 0.3.0-draft.2 (dth_sc.py, dth_pc.py, dth_phc.py)
EXISTING = {
    "nra": "id-8e67c8e9e1195cdc857b03a2c640e7fe",                     # National Regulatory Authority (BusinessRole, dth_sc.py; id-sc-role-nmra)
    "product-registry": "id-59c26d672a4248e0bb83cf4d26cba10c",        # Product Registry (ApplicationComponent, 0.2.0)
    "facility-registry": "id-5f6d9b9678824b37b95952735420ae8d",       # Facility registry (ApplicationComponent, 0.2.0)
    "hwr": "id-350840520ae44f658b6ad3b3762e382e",                     # DPI-H Health Workforce Registry (HWR) (ApplicationComponent, 0.2.0)
    "terminology-service": "id-3f41de2b51c24041b08243bf72b140d1",     # Terminology Service (ApplicationComponent, 0.2.0)
    "interop-component": "id-80856538cbd44167a37b276e38c994c3",       # Interoperability Component (ApplicationComponent, 0.2.0)
    "identity-mgmt-service": "id-646c18afcfc54f4fb33ae93110e02c2c",   # Identity Management Service (ApplicationService, 0.2.0)
    "update-subscription": "id-6b78a242e71a428c87434e2fe5891ee2",     # Update Subscription/Notification (ApplicationService, 0.2.0)
    "security-consent-module": "id-d79aa0eec0584b0792b44bca408afeb6", # DPI-F Security & Consent Module (ApplicationComponent, 0.2.0)
    "cap-recall": "id-a9c92f8fa2924d4180e8f5512b0d0097",              # Recall (Capability, 0.2.0)
    "cap-traceability": "id-e88f6d077d31407bb1af5f2ecfd3b48a",        # Traceability (Capability, 0.2.0)
    "cap-pmdm": "id-366955c9809942bc8a57d0a77c11d202",                # Product Master Data Management (Capability, 0.2.0)
    "moh": "id-1c5c0bc9234e4282b654dbc71b9da706",                     # Ministry of Health (Stakeholder, 0.2.0)
    "health-workers-sh": "id-8d3dd8b68d504c2a9fe8cf414b16c127",       # Health Workers (Stakeholder, 0.2.0)
    "patients": "id-a2320dbc07e6450b94f3f0f3e03bb877",                # Patients (Stakeholder, 0.2.0)
    "licensing-bodies": "id-63c448813aea4067bb68281f7926fd2b",        # Licensing Bodies (Stakeholder, 0.2.0)
    "trade-item": "id-60e7d1d9e64c5011a1efe8becac406d0",              # Trade Item (BusinessObject, dth_pc.py)
    "traceability-event": "id-5dc77dae1bce5d11b288830795b31bdf",      # Traceability Event (DataObject, dth_sc.py)
    "regulatory-systems": "id-22eff58eae365a4f8d0e0368d8c3497e",      # Regulatory Systems (ApplicationComponent, dth_sc.py)
    "quality-systems": "id-1555c26cfbcd57f49b6e63fed8491d80",         # Quality Systems (ApplicationComponent, dth_sc.py)
    "product-verification": "id-975c5567001151299672c0341a733111",    # Product Verification (ApplicationService, dth_sc.py)
    "pos-app": "id-808925f4d2075d7b95e0651ebae00fcf",                 # Point-of-service application (ApplicationComponent, dth_phc.py)
    "health-worker": "id-54d7e249c99a59c6a2085f17060de254",           # Health worker (BusinessRole, dth_phc.py)
}

EXISTING_RELATIONS = {
    ("Serving", "cap-pmdm", "cap-traceability"): "id-2218b6c85880458d9d995de0a0e1b049",
    ("Access", "product-verification", "traceability-event"): "id-25d00334b7355e66b67722087d9a16fe",
    ("Serving", "product-verification", "nra"): "id-5965c2951caf5848840ba9c82648b6a6",
    ("Flow", "pos-app", "interop-component"): "id-433fffbfdeb156e79a0dd82c64ff3b69",
    ("Serving", "hwr", "interop-component"): "id-067ea908bb7f51b3b52068d5be84c223",
    ("Serving", "terminology-service", "interop-component"): "id-d4d703c340a3507692f4ca468119a2cd",
    ("Serving", "pos-app", "health-worker"): "id-3ef6ed3b1b9c59adb6ca9015e1388379",
    ("Association", "health-worker", "health-workers-sh"): "id-c13f077bb0065095bcdbb8d7890250d2",
}

# View 1: SF Reporting in the DIIG Enterprise Architecture (DTH SFP Fig. 3)
V1_DRAWN = [
    ("Specialization", "sf-reporting-app", "pos-app"),
    ("Serving", "sf-reporting-app", "hcp-reporter"),
    ("Realization", "sf-reporting-app", "cap-sf-case-reporting"),
    ("Serving", "identity-mgmt-service", "sf-reporting-app"),
    ("Flow", "sf-reporting-app", "nmra-case-mgmt-backend"),
    ("Realization", "nmra-case-mgmt-backend", "cap-sf-case-reporting"),
    ("Realization", "nmra-case-mgmt-backend", "cap-post-market-surveillance"),
    ("Flow", "nmra-case-mgmt-backend", "pv-system"),
    ("Realization", "pv-system", "cap-post-market-surveillance"),
    ("Realization", "pv-system", "cap-pharmacovigilance"),
    ("Aggregation", "regulatory-systems", "pv-system"),
    ("Realization", "regulatory-systems", "cap-pharmacovigilance"),
    ("Realization", "security-consent-module", "identity-mgmt-service"),
    ("Serving", "hwr", "identity-mgmt-service"),
    ("Serving", "hwr", "interop-component"),
    ("Flow", "nmra-case-mgmt-backend", "interop-component"),
    ("Flow", "pv-system", "interop-component"),
    ("Serving", "update-subscription", "pv-system"),
    ("Serving", "update-subscription", "interop-component"),
    ("Flow", "quality-systems", "regulatory-systems"),
    ("Serving", "update-subscription", "quality-systems"),
    ("Realization", "product-registry", "cap-pmdm"),
    ("Serving", "product-registry", "interop-component"),
    ("Serving", "facility-registry", "interop-component"),
    ("Serving", "terminology-service", "interop-component"),
    ("Realization", "quality-systems", "cap-recall"),
]

# View 2: SF Reporting Business Process View (DTH SFP Fig. 4 & SF-REP-001..006)
V2_DRAWN = [
    ("Triggering", "sf-rep-001", "sf-rep-002"),
    ("Triggering", "sf-rep-002", "sf-rep-003"),
    ("Triggering", "sf-rep-003", "sf-rep-004"),
    ("Triggering", "sf-rep-004", "sf-rep-005"),
    ("Triggering", "sf-rep-005", "sf-rep-006"),
    ("Assignment", "hcp-reporter", "sf-rep-001"),
    ("Serving", "sf-rep-006", "hcp-reporter"),
    ("Association", "hcp-reporter", "patients", {"name": "advises patient"}),
    ("Association", "hcp-reporter", "health-workers-sh", {"name": "candidateMatch"}),
    ("Realization", "sf-rep-001", "cap-sf-case-reporting"),
    ("Access", "sf-rep-001", "trade-item", {"accessType": 1}),
    ("Access", "sf-rep-002", "trade-item", {"accessType": 1}),
    ("Access", "sf-rep-002", "bo-sf-report", {"accessType": 3}),
    ("Access", "sf-rep-003", "bo-sf-report", {"accessType": 1}),
    ("Realization", "sf-rep-003", "cap-sf-case-investigation"),
    ("Assignment", "nmra-reviewer", "sf-rep-003"),
    ("Assignment", "nmra-reviewer", "sf-rep-004"),
    ("Aggregation", "nra", "nmra-reviewer"),
    ("Assignment", "nra", "sf-rep-004"),
    ("Realization", "sf-rep-006", "cap-traceability"),
    ("Access", "sf-rep-006", "bo-medical-product-alert", {"accessType": 1}),
    ("Access", "sf-rep-005", "bo-medical-product-alert", {"accessType": 2}),
    ("Realization", "sf-rep-005", "cap-recall"),
    ("Realization", "sf-rep-005", "cap-regulatory-enforcement"),
    ("Aggregation", "cap-regulatory-enforcement", "cap-recall"),
    ("Realization", "sf-rep-004", "cap-regulatory-enforcement"),
    ("Association", "nra", "law-enforcement-customs", {"name": "joint investigation & referral"}),
    ("Association", "sf-rep-004", "law-enforcement-customs", {"name": "criminal referral"}),
]

# View 3: SF Reporting Application Cooperation View
V3_DRAWN = [
    ("Association", "do-sf-report", "trade-item", {"name": "DE3 Product ID / DE5 Type"}),
    ("Association", "do-sf-report", "traceability-event", {"name": "DE3 Product ID, DE6 Batch, DE7 Expiry"}),
    ("Access", "product-verification", "traceability-event", {"accessType": 1}),
    ("Access", "sf-reporting-app", "do-sf-report", {"accessType": 3}),
    ("Serving", "product-verification", "sf-reporting-app"),
    ("Flow", "sf-reporting-app", "nmra-case-mgmt-backend"),
    ("Flow", "who-medical-product-alert-system", "sf-reporting-app"),
    ("Flow", "who-medical-product-alert-system", "nmra-case-mgmt-backend"),
    ("Flow", "who-gsms", "who-medical-product-alert-system"),
    ("Flow", "nmra-case-mgmt-backend", "who-gsms"),
    ("Serving", "product-registry", "product-verification"),
    ("Serving", "product-registry", "interop-component"),
    ("Flow", "interop-component", "nmra-case-mgmt-backend"),
    ("Flow", "nmra-case-mgmt-backend", "pv-system"),
    ("Flow", "interop-component", "pv-system"),
    ("Flow", "pv-system", "vigiflow-vigibase"),
    ("Flow", "pv-system", "who-gsms"),
    ("Serving", "facility-registry", "interop-component"),
    ("Serving", "hwr", "interop-component"),
    ("Serving", "terminology-service", "interop-component"),
    ("Serving", "terminology-service", "pv-system"),
    ("Aggregation", "regulatory-systems", "pv-system"),
    ("Flow", "regulatory-systems", "vigiflow-vigibase"),
]

# View 4: SF Reporting Regulatory Governance View (DTH SFP §2.3)
V4_DRAWN = [
    ("Association", "regional-global-regulators", "moh", {"name": "harmonize regulations"}),
    ("Association", "regional-global-regulators", "nra", {"name": "harmonize regulations and alerts"}),
    ("Association", "law-enforcement-customs", "nra", {"name": "joint investigations and border control"}),
    ("Association", "moh", "nra", {"name": "policy and funding support"}),
    ("Association", "moh", "steering-committee", {"name": "leads"}),
    ("Aggregation", "steering-committee", "nra"),
    ("Association", "ict-ministry", "steering-committee", {"name": "eHealth strategy alignment"}),
    ("Association", "ict-ministry", "technical-working-group", {"name": "IT and infrastructure specialists"}),
    ("Serving", "technical-working-group", "steering-committee"),
    ("Association", "health-financing-procurement", "technical-working-group", {"name": "supply chain and reimbursement alignment"}),
    ("Association", "professional-associations", "advisory-council", {"name": "member"}),
    ("Serving", "advisory-council", "technical-working-group"),
    ("Association", "professional-associations", "project-champion", {"name": "engaged by"}),
    ("Association", "medical-product-industry", "project-champion", {"name": "engaged by"}),
    ("Serving", "project-champion", "advisory-council"),
    ("Realization", "nra", "goal-timely-regulatory-action"),
    ("Influence", "nra", "driver-patient-safety"),
    ("Influence", "goal-timely-regulatory-action", "driver-patient-safety"),
    ("Influence", "steering-committee", "driver-patient-safety"),
    ("Realization", "steering-committee", "goal-reduced-detection-to-notification-time"),
    ("Influence", "goal-reduced-detection-to-notification-time", "driver-patient-safety"),
    ("Serving", "digital-health-coordinator", "steering-committee"),
    ("Serving", "digital-health-coordinator", "technical-working-group"),
    ("Realization", "digital-health-coordinator", "goal-reduced-detection-to-notification-time"),
    ("Realization", "digital-health-coordinator", "goal-supply-chain-transparency"),
    ("Influence", "advisory-council", "goal-supply-chain-transparency"),
    ("Influence", "project-champion", "goal-supply-chain-transparency"),
    ("Association", "licensing-bodies", "project-champion", {"name": "professional credential alignment"}),
    ("Influence", "assessment-trust-incentives-barriers", "goal-timely-regulatory-action"),
    ("Influence", "assessment-trust-incentives-barriers", "driver-patient-safety"),
    ("Association", "patients", "driver-patient-safety"),
    ("Influence", "assessment-process-operational-barriers", "driver-patient-safety"),
    ("Influence", "assessment-process-operational-barriers", "goal-reduced-detection-to-notification-time"),
    ("Influence", "assessment-technical-infrastructure-barriers", "goal-reduced-detection-to-notification-time"),
    ("Association", "digital-health-coordinator", "assessment-technical-infrastructure-barriers"),
    ("Influence", "assessment-awareness-knowledge-barriers", "goal-supply-chain-transparency"),
    ("Association", "digital-health-coordinator", "assessment-awareness-knowledge-barriers"),
    ("Association", "health-workers-sh", "assessment-awareness-knowledge-barriers"),
    ("Association", "health-workers-sh", "licensing-bodies"),
    ("Association", "health-workers-sh", "goal-supply-chain-transparency"),
]

MODEL_ONLY = [
    ("Aggregation", "regulatory-systems", "nmra-case-mgmt-backend"),
    ("Realization", "regulatory-systems", "cap-post-market-surveillance"),
    ("Realization", "regulatory-systems", "cap-recall"),
    ("Realization", "regulatory-systems", "cap-regulatory-enforcement"),
    ("Realization", "do-sf-report", "bo-sf-report"),
    ("Access", "nmra-case-mgmt-backend", "do-sf-report", {"accessType": 3}),
    ("Access", "sf-rep-001", "bo-sf-report", {"accessType": 3}),
    ("Access", "sf-rep-004", "bo-sf-report", {"accessType": 3}),
    ("Access", "sf-rep-005", "bo-sf-report", {"accessType": 1}),
    ("Access", "sf-rep-006", "bo-sf-report", {"accessType": 1}),
    ("Assignment", "hcp-reporter", "sf-rep-002"),
    ("Assignment", "nra", "sf-rep-005"),
    ("Assignment", "nra", "sf-rep-006"),
    ("Realization", "sf-rep-004", "cap-sf-case-investigation"),
    ("Realization", "sf-reporting-app", "sf-rep-001"),
    ("Realization", "sf-reporting-app", "sf-rep-002"),
    ("Realization", "nmra-case-mgmt-backend", "sf-rep-003"),
    ("Realization", "nmra-case-mgmt-backend", "sf-rep-004"),
    ("Realization", "nmra-case-mgmt-backend", "sf-rep-005"),
    ("Realization", "nmra-case-mgmt-backend", "sf-rep-006"),
    ("Realization", "cap-sf-case-reporting", "goal-reduced-detection-to-notification-time"),
    ("Realization", "cap-sf-case-investigation", "goal-timely-regulatory-action"),
    ("Realization", "cap-regulatory-enforcement", "goal-timely-regulatory-action"),
    ("Realization", "cap-post-market-surveillance", "goal-supply-chain-transparency"),
    ("Association", "hcp-reporter", "health-worker", {"name": "candidateMatch"}),
]

_seen = set(EXISTING_RELATIONS.keys())
RELATIONS = []
for r in V1_DRAWN + V2_DRAWN + V3_DRAWN + V4_DRAWN + MODEL_ONLY:
    k = (r[0], r[1], r[2])
    if k not in _seen:
        _seen.add(k)
        RELATIONS.append(r)


def b(key):
    return ("box", key)


def boxes(*keys):
    return [b(k) for k in keys]


V_DIIG_EA = "SF Reporting in the DIIG Enterprise Architecture (DTH SFP Fig. 3)"
V_BUSINESS = "SF Reporting Business Process View (DTH SFP Fig. 4 & SF-REP-001..006)"
V_APP_COOP = "SF Reporting Application Cooperation View"
V_GOVERNANCE = "SF Reporting Regulatory Governance View (DTH SFP §2.3)"

VIEWS = [
    (
        V_DIIG_EA,
        "Substandard and falsified (SF) medical product reporting within the DIIG Digital Health Enterprise Architecture Framework (Section 3.2, Fig. 3, PDF 33-34): placing the SF Reporting Application in the Point-of-Service layer (specializing Point-of-service application), the NMRA Case Management Back End and Pharmacovigilance System in the Business Domain Services layer (linked into dth-sc Regulatory Systems and Quality Systems), and DPI-H registries (Product Registry, DPI-H Health Workforce Registry, Facility registry), Terminology Service, Identity Management Service, DPI-F Security & Consent Module, Update Subscription/Notification, and Interoperability Component in the foundational and interoperability layers.",
        (
            "col",
            [
                ("row", boxes("pos-app", "sf-reporting-app", "cap-sf-case-reporting", "cap-post-market-surveillance", "cap-pharmacovigilance")),
                ("row", boxes("hcp-reporter", "identity-mgmt-service", "nmra-case-mgmt-backend", "pv-system", "regulatory-systems")),
                ("row", boxes("security-consent-module", "hwr", "interop-component", "update-subscription", "quality-systems")),
                ("row", boxes("cap-pmdm", "product-registry", "facility-registry", "terminology-service", "cap-recall")),
            ],
        ),
    ),
    (
        V_BUSINESS,
        "End-to-end business process view for reporting and acting on suspected substandard and falsified medical products (Table 10, Fig. 4, Table 9, Intro p. 1, Section 2.1-2.2, Section 2.4; PDF 13, 27-28, 39-43): roles (Health Care Professional (Reporter), NMRA Reviewer, National Regulatory Authority), processes SF-REP-001 through SF-REP-006, business objects (SF Report, Medical Product Alert, Trade Item), and realized capabilities (SF Case Reporting, SF Case Investigation, Regulatory Enforcement, Recall, Traceability).",
        (
            "col",
            [
                ("row", boxes("patients", "cap-sf-case-reporting", "trade-item", "bo-sf-report", "cap-sf-case-investigation")),
                ("row", boxes("hcp-reporter", "sf-rep-001", "sf-rep-002", "sf-rep-003", "nmra-reviewer")),
                ("row", boxes("health-workers-sh", "sf-rep-006", "sf-rep-005", "sf-rep-004", "nra")),
                ("row", boxes("cap-traceability", "bo-medical-product-alert", "cap-recall", "cap-regulatory-enforcement", "law-enforcement-customs")),
            ],
        ),
    ),
    (
        V_APP_COOP,
        "Application cooperation and data exchange view for substandard and falsified medical product reporting (Section 1.3, Table 4, Section 3.2, Section 4.4, Table 11, Ch. 7; PDF 22, 24, 33-34, 42-43, 59): SF Reporting Application, NMRA Case Management Back End, Pharmacovigilance System, SF Report Data Object (SFR.A1.DE1..DE10, linked to Trade Item and Traceability Event), Product Verification, shared DPI-H registries (Product Registry, DPI-H Health Workforce Registry, Facility registry, Terminology Service) via the Interoperability Component, and external WHO systems (WHO GSMS, VigiFlow / VigiBase, WHO Medical Product Alert System).",
        (
            "col",
            [
                ("row", boxes("trade-item", "do-sf-report", "sf-reporting-app", "who-medical-product-alert-system")),
                ("row", boxes("traceability-event", "product-verification", "nmra-case-mgmt-backend", "who-gsms")),
                ("row", boxes("product-registry", "interop-component", "pv-system", "vigiflow-vigibase")),
                ("row", boxes("facility-registry", "hwr", "terminology-service", "regulatory-systems")),
            ],
        ),
    ),
    (
        V_GOVERNANCE,
        "Regulatory governance, multisectoral stakeholder alignment, strategic goals, and reporting barrier assessments for substandard and falsified medical products reporting (Section 1.1, Table 5, Section 2.2-2.4, Annex 4, Annex 6; PDF 20, 25, 28, 68, 70): Ministry of Health, National Regulatory Authority, Steering Committee, Technical Working Group, Advisory Council, Project Champion, Digital Health Coordinator, multisectoral stakeholders (Law Enforcement and Customs, Professional Associations, Medical Product Industry, Health Financing and Procurement Agencies, ICT Ministry, Regional and Global Regulators, Licensing Bodies, Health Workers, Patients), strategic driver and goals (Patient Safety, Timely Regulatory Action, Supply Chain Transparency, Reduced Detection-to-Notification Time), and Table 5 barrier assessments.",
        (
            "col",
            [
                ("row", boxes("regional-global-regulators", "moh", "ict-ministry", "health-financing-procurement", "professional-associations", "medical-product-industry")),
                ("row", boxes("law-enforcement-customs", "nra", "steering-committee", "technical-working-group", "advisory-council", "project-champion")),
                ("row", boxes("goal-timely-regulatory-action", "driver-patient-safety", "goal-reduced-detection-to-notification-time", "digital-health-coordinator", "goal-supply-chain-transparency", "licensing-bodies")),
                ("row", boxes("assessment-trust-incentives-barriers", "patients", "assessment-process-operational-barriers", "assessment-technical-infrastructure-barriers", "assessment-awareness-knowledge-barriers", "health-workers-sh")),
            ],
        ),
    ),
]

VIEW_CONNECTIONS = {
    V_DIIG_EA: V1_DRAWN,
    V_BUSINESS: V2_DRAWN,
    V_APP_COOP: V3_DRAWN,
    V_GOVERNANCE: V4_DRAWN,
}
