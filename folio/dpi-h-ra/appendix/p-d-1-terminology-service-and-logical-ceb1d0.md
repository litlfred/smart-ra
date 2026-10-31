- **WHO ICD API and local deployments —** WHO services exposing ICD-11 Foundation and MMS content, identifiers, releases, search, and coding-related information. The API can be accessed through WHO-hosted services or suitable local deployments, including operation without a continuous external connection. It provides a concrete implementation route for an ICD-11-based semantic service. Implementers should declare the supported content, release, language, and operations. The separately documented WHO FHIR interface is under active development; implementations relying on it should declare its FHIR version, release coverage, publication status and tested operations at the time of implementation.[^86a]
- **WHO ICD-11 Coding Tool and Embedded Coding Tool —** tools supporting selection of ICD-11 concepts and applicable coding detail within clinical applications. An implementation should select the appropriate coding workflow and retain its resulting identifiers and expressions. A simplified search interface should not be represented as providing the full medical-coding workflow.[^86b]
- **Snowstorm —** an open-source, FHIR-conformant terminology server used by national terminology services to host SNOMED CT and national extensions.[^86]
- **Ontoserver** **—** a FHIR-conformant terminology server adopted as a national terminology service in Australia and used in several other jurisdictions.[^87]
- **HL7 FHIR reference terminology service (tx.fhir.org) —** the reference implementation of the FHIR Terminology Service specification, widely used for testing and reference.[^88]
- **openEHR** **Clinical Knowledge Manager —** an international, peer-reviewed repository of archetypes and templates supporting local adaptation of globally curated models.[^89]
- **National FHIR profile registries —** country-specific implementation guides and profiles (for example, Simplifier-based national registries), maintaining canonical structural definitions.

[^86a]: https://icd.who.int/docs/icd-api/APIDoc-Version2/ ; https://icd.who.int/docs/icd-api/ICDAPI-LocalDeployment/ ; https://icd.who.int/docs/icd-api/ICDAPI-FHIR-Support/
[^86b]: https://icd.who.int/docs/icd-api/icd11ect-1.8/EmbeddedCodingTool/
[^86]: https://github.com/IHTSDO/snowstorm
[^87]: https://ontoserver.csiro.au/
[^88]: https://tx.fhir.org/
[^89]: https://ckm.openehr.org/ckm/
