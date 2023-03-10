# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openziti_edge_management.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openziti_edge_management.model.api_error import ApiError
from openziti_edge_management.model.api_error_args import ApiErrorArgs
from openziti_edge_management.model.api_error_cause import ApiErrorCause
from openziti_edge_management.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_management.model.api_field_error import ApiFieldError
from openziti_edge_management.model.api_session_detail import ApiSessionDetail
from openziti_edge_management.model.api_session_detail_all_of import ApiSessionDetailAllOf
from openziti_edge_management.model.api_session_list import ApiSessionList
from openziti_edge_management.model.api_session_posture_data import ApiSessionPostureData
from openziti_edge_management.model.api_version import ApiVersion
from openziti_edge_management.model.attributes import Attributes
from openziti_edge_management.model.auth_policy_create import AuthPolicyCreate
from openziti_edge_management.model.auth_policy_detail import AuthPolicyDetail
from openziti_edge_management.model.auth_policy_detail_all_of import AuthPolicyDetailAllOf
from openziti_edge_management.model.auth_policy_list import AuthPolicyList
from openziti_edge_management.model.auth_policy_patch import AuthPolicyPatch
from openziti_edge_management.model.auth_policy_primary import AuthPolicyPrimary
from openziti_edge_management.model.auth_policy_primary_cert import AuthPolicyPrimaryCert
from openziti_edge_management.model.auth_policy_primary_cert_patch import AuthPolicyPrimaryCertPatch
from openziti_edge_management.model.auth_policy_primary_ext_jwt import AuthPolicyPrimaryExtJwt
from openziti_edge_management.model.auth_policy_primary_ext_jwt_patch import AuthPolicyPrimaryExtJwtPatch
from openziti_edge_management.model.auth_policy_primary_patch import AuthPolicyPrimaryPatch
from openziti_edge_management.model.auth_policy_primary_updb import AuthPolicyPrimaryUpdb
from openziti_edge_management.model.auth_policy_primary_updb_patch import AuthPolicyPrimaryUpdbPatch
from openziti_edge_management.model.auth_policy_secondary import AuthPolicySecondary
from openziti_edge_management.model.auth_policy_secondary_patch import AuthPolicySecondaryPatch
from openziti_edge_management.model.auth_policy_update import AuthPolicyUpdate
from openziti_edge_management.model.auth_query_detail import AuthQueryDetail
from openziti_edge_management.model.auth_query_list import AuthQueryList
from openziti_edge_management.model.authenticate import Authenticate
from openziti_edge_management.model.authenticator_create import AuthenticatorCreate
from openziti_edge_management.model.authenticator_detail import AuthenticatorDetail
from openziti_edge_management.model.authenticator_detail_all_of import AuthenticatorDetailAllOf
from openziti_edge_management.model.authenticator_list import AuthenticatorList
from openziti_edge_management.model.authenticator_patch import AuthenticatorPatch
from openziti_edge_management.model.authenticator_patch_with_current import AuthenticatorPatchWithCurrent
from openziti_edge_management.model.authenticator_patch_with_current_all_of import AuthenticatorPatchWithCurrentAllOf
from openziti_edge_management.model.authenticator_update import AuthenticatorUpdate
from openziti_edge_management.model.authenticator_update_with_current import AuthenticatorUpdateWithCurrent
from openziti_edge_management.model.base_entity import BaseEntity
from openziti_edge_management.model.ca_create import CaCreate
from openziti_edge_management.model.ca_detail import CaDetail
from openziti_edge_management.model.ca_detail_all_of import CaDetailAllOf
from openziti_edge_management.model.ca_list import CaList
from openziti_edge_management.model.ca_patch import CaPatch
from openziti_edge_management.model.ca_update import CaUpdate
from openziti_edge_management.model.common_edge_router_properties import CommonEdgeRouterProperties
from openziti_edge_management.model.config_create import ConfigCreate
from openziti_edge_management.model.config_detail import ConfigDetail
from openziti_edge_management.model.config_detail_all_of import ConfigDetailAllOf
from openziti_edge_management.model.config_list import ConfigList
from openziti_edge_management.model.config_patch import ConfigPatch
from openziti_edge_management.model.config_type_create import ConfigTypeCreate
from openziti_edge_management.model.config_type_detail import ConfigTypeDetail
from openziti_edge_management.model.config_type_detail_all_of import ConfigTypeDetailAllOf
from openziti_edge_management.model.config_type_list import ConfigTypeList
from openziti_edge_management.model.config_type_patch import ConfigTypePatch
from openziti_edge_management.model.config_type_update import ConfigTypeUpdate
from openziti_edge_management.model.config_types import ConfigTypes
from openziti_edge_management.model.config_update import ConfigUpdate
from openziti_edge_management.model.create_envelope import CreateEnvelope
from openziti_edge_management.model.create_location import CreateLocation
from openziti_edge_management.model.current_api_session_detail import CurrentApiSessionDetail
from openziti_edge_management.model.current_api_session_detail_all_of import CurrentApiSessionDetailAllOf
from openziti_edge_management.model.current_api_session_detail_envelope import CurrentApiSessionDetailEnvelope
from openziti_edge_management.model.current_identity_detail_envelope import CurrentIdentityDetailEnvelope
from openziti_edge_management.model.data_integrity_check_detail import DataIntegrityCheckDetail
from openziti_edge_management.model.data_integrity_check_detail_list import DataIntegrityCheckDetailList
from openziti_edge_management.model.data_integrity_check_details import DataIntegrityCheckDetails
from openziti_edge_management.model.data_integrity_check_result_envelope import DataIntegrityCheckResultEnvelope
from openziti_edge_management.model.detail_api_session_envelope import DetailApiSessionEnvelope
from openziti_edge_management.model.detail_auth_policy_envelope import DetailAuthPolicyEnvelope
from openziti_edge_management.model.detail_authenticator_envelope import DetailAuthenticatorEnvelope
from openziti_edge_management.model.detail_ca_envelope import DetailCaEnvelope
from openziti_edge_management.model.detail_config_envelope import DetailConfigEnvelope
from openziti_edge_management.model.detail_config_type_envelope import DetailConfigTypeEnvelope
from openziti_edge_management.model.detail_edge_router_policy_envelope import DetailEdgeRouterPolicyEnvelope
from openziti_edge_management.model.detail_enrollment_envelope import DetailEnrollmentEnvelope
from openziti_edge_management.model.detail_external_jwt_signer_envelope import DetailExternalJwtSignerEnvelope
from openziti_edge_management.model.detail_identity_envelope import DetailIdentityEnvelope
from openziti_edge_management.model.detail_identity_type_envelope import DetailIdentityTypeEnvelope
from openziti_edge_management.model.detail_mfa import DetailMfa
from openziti_edge_management.model.detail_mfa_all_of import DetailMfaAllOf
from openziti_edge_management.model.detail_mfa_envelope import DetailMfaEnvelope
from openziti_edge_management.model.detail_mfa_recovery_codes import DetailMfaRecoveryCodes
from openziti_edge_management.model.detail_mfa_recovery_codes_all_of import DetailMfaRecoveryCodesAllOf
from openziti_edge_management.model.detail_mfa_recovery_codes_envelope import DetailMfaRecoveryCodesEnvelope
from openziti_edge_management.model.detail_posture_check_envelope import DetailPostureCheckEnvelope
from openziti_edge_management.model.detail_posture_check_type_envelope import DetailPostureCheckTypeEnvelope
from openziti_edge_management.model.detail_router_envelope import DetailRouterEnvelope
from openziti_edge_management.model.detail_service_edge_policy_envelope import DetailServiceEdgePolicyEnvelope
from openziti_edge_management.model.detail_service_envelope import DetailServiceEnvelope
from openziti_edge_management.model.detail_service_policy_envelop import DetailServicePolicyEnvelop
from openziti_edge_management.model.detail_session_management_envelope import DetailSessionManagementEnvelope
from openziti_edge_management.model.detail_session_route_path_envelope import DetailSessionRoutePathEnvelope
from openziti_edge_management.model.detail_spec_body_envelope import DetailSpecBodyEnvelope
from openziti_edge_management.model.detail_spec_envelope import DetailSpecEnvelope
from openziti_edge_management.model.detail_terminator_envelope import DetailTerminatorEnvelope
from openziti_edge_management.model.detailed_edge_router_envelope import DetailedEdgeRouterEnvelope
from openziti_edge_management.model.dial_bind import DialBind
from openziti_edge_management.model.dial_bind_array import DialBindArray
from openziti_edge_management.model.disable_params import DisableParams
from openziti_edge_management.model.edge_router_create import EdgeRouterCreate
from openziti_edge_management.model.edge_router_detail import EdgeRouterDetail
from openziti_edge_management.model.edge_router_detail_all_of import EdgeRouterDetailAllOf
from openziti_edge_management.model.edge_router_list import EdgeRouterList
from openziti_edge_management.model.edge_router_patch import EdgeRouterPatch
from openziti_edge_management.model.edge_router_policy_create import EdgeRouterPolicyCreate
from openziti_edge_management.model.edge_router_policy_detail import EdgeRouterPolicyDetail
from openziti_edge_management.model.edge_router_policy_detail_all_of import EdgeRouterPolicyDetailAllOf
from openziti_edge_management.model.edge_router_policy_list import EdgeRouterPolicyList
from openziti_edge_management.model.edge_router_policy_patch import EdgeRouterPolicyPatch
from openziti_edge_management.model.edge_router_policy_update import EdgeRouterPolicyUpdate
from openziti_edge_management.model.edge_router_update import EdgeRouterUpdate
from openziti_edge_management.model.empty import Empty
from openziti_edge_management.model.enrollment_create import EnrollmentCreate
from openziti_edge_management.model.enrollment_detail import EnrollmentDetail
from openziti_edge_management.model.enrollment_detail_all_of import EnrollmentDetailAllOf
from openziti_edge_management.model.enrollment_list import EnrollmentList
from openziti_edge_management.model.enrollment_refresh import EnrollmentRefresh
from openziti_edge_management.model.entity_ref import EntityRef
from openziti_edge_management.model.env_info import EnvInfo
from openziti_edge_management.model.external_id_claim import ExternalIdClaim
from openziti_edge_management.model.external_id_claim_patch import ExternalIdClaimPatch
from openziti_edge_management.model.external_jwt_signer_create import ExternalJwtSignerCreate
from openziti_edge_management.model.external_jwt_signer_detail import ExternalJwtSignerDetail
from openziti_edge_management.model.external_jwt_signer_detail_all_of import ExternalJwtSignerDetailAllOf
from openziti_edge_management.model.external_jwt_signer_list import ExternalJwtSignerList
from openziti_edge_management.model.external_jwt_signer_patch import ExternalJwtSignerPatch
from openziti_edge_management.model.external_jwt_signer_update import ExternalJwtSignerUpdate
from openziti_edge_management.model.failed_service_request import FailedServiceRequest
from openziti_edge_management.model.failed_service_request_envelope import FailedServiceRequestEnvelope
from openziti_edge_management.model.failed_service_request_list import FailedServiceRequestList
from openziti_edge_management.model.get_identity_policy_advice_envelope import GetIdentityPolicyAdviceEnvelope
from openziti_edge_management.model.identity_authenticators import IdentityAuthenticators
from openziti_edge_management.model.identity_authenticators_cert import IdentityAuthenticatorsCert
from openziti_edge_management.model.identity_authenticators_updb import IdentityAuthenticatorsUpdb
from openziti_edge_management.model.identity_create import IdentityCreate
from openziti_edge_management.model.identity_create_enrollment import IdentityCreateEnrollment
from openziti_edge_management.model.identity_detail import IdentityDetail
from openziti_edge_management.model.identity_detail_all_of import IdentityDetailAllOf
from openziti_edge_management.model.identity_enrollments import IdentityEnrollments
from openziti_edge_management.model.identity_enrollments_ott import IdentityEnrollmentsOtt
from openziti_edge_management.model.identity_enrollments_ottca import IdentityEnrollmentsOttca
from openziti_edge_management.model.identity_extend_certs import IdentityExtendCerts
from openziti_edge_management.model.identity_extend_enrollment_envelope import IdentityExtendEnrollmentEnvelope
from openziti_edge_management.model.identity_extend_enrollment_request import IdentityExtendEnrollmentRequest
from openziti_edge_management.model.identity_extend_validate_enrollment_request import IdentityExtendValidateEnrollmentRequest
from openziti_edge_management.model.identity_list import IdentityList
from openziti_edge_management.model.identity_patch import IdentityPatch
from openziti_edge_management.model.identity_type import IdentityType
from openziti_edge_management.model.identity_type_detail import IdentityTypeDetail
from openziti_edge_management.model.identity_type_detail_all_of import IdentityTypeDetailAllOf
from openziti_edge_management.model.identity_type_list import IdentityTypeList
from openziti_edge_management.model.identity_update import IdentityUpdate
from openziti_edge_management.model.link import Link
from openziti_edge_management.model.links import Links
from openziti_edge_management.model.list_api_sessions_envelope import ListApiSessionsEnvelope
from openziti_edge_management.model.list_auth_policies_envelope import ListAuthPoliciesEnvelope
from openziti_edge_management.model.list_authenticators_envelope import ListAuthenticatorsEnvelope
from openziti_edge_management.model.list_cas_envelope import ListCasEnvelope
from openziti_edge_management.model.list_config_types_envelope import ListConfigTypesEnvelope
from openziti_edge_management.model.list_configs_envelope import ListConfigsEnvelope
from openziti_edge_management.model.list_edge_router_policies_envelope import ListEdgeRouterPoliciesEnvelope
from openziti_edge_management.model.list_edge_routers_envelope import ListEdgeRoutersEnvelope
from openziti_edge_management.model.list_enrollments_envelope import ListEnrollmentsEnvelope
from openziti_edge_management.model.list_external_jwt_signers_envelope import ListExternalJwtSignersEnvelope
from openziti_edge_management.model.list_identities_envelope import ListIdentitiesEnvelope
from openziti_edge_management.model.list_identity_types_envelope import ListIdentityTypesEnvelope
from openziti_edge_management.model.list_posture_check_envelope import ListPostureCheckEnvelope
from openziti_edge_management.model.list_posture_check_types_envelope import ListPostureCheckTypesEnvelope
from openziti_edge_management.model.list_role_attributes_envelope import ListRoleAttributesEnvelope
from openziti_edge_management.model.list_routers_envelope import ListRoutersEnvelope
from openziti_edge_management.model.list_service_configs_envelope import ListServiceConfigsEnvelope
from openziti_edge_management.model.list_service_edge_router_policies_envelope import ListServiceEdgeRouterPoliciesEnvelope
from openziti_edge_management.model.list_service_policies_envelope import ListServicePoliciesEnvelope
from openziti_edge_management.model.list_services_envelope import ListServicesEnvelope
from openziti_edge_management.model.list_sessions_management_envelope import ListSessionsManagementEnvelope
from openziti_edge_management.model.list_specs_envelope import ListSpecsEnvelope
from openziti_edge_management.model.list_summary_counts import ListSummaryCounts
from openziti_edge_management.model.list_summary_counts_envelope import ListSummaryCountsEnvelope
from openziti_edge_management.model.list_terminators_envelope import ListTerminatorsEnvelope
from openziti_edge_management.model.list_version_envelope import ListVersionEnvelope
from openziti_edge_management.model.meta import Meta
from openziti_edge_management.model.mfa_code import MfaCode
from openziti_edge_management.model.mfa_formats import MfaFormats
from openziti_edge_management.model.mfa_providers import MfaProviders
from openziti_edge_management.model.named_role import NamedRole
from openziti_edge_management.model.named_roles import NamedRoles
from openziti_edge_management.model.operating_system import OperatingSystem
from openziti_edge_management.model.os_type import OsType
from openziti_edge_management.model.pagination import Pagination
from openziti_edge_management.model.password import Password
from openziti_edge_management.model.password_nullable import PasswordNullable
from openziti_edge_management.model.policy_advice import PolicyAdvice
from openziti_edge_management.model.policy_failure import PolicyFailure
from openziti_edge_management.model.posture_check_create import PostureCheckCreate
from openziti_edge_management.model.posture_check_detail import PostureCheckDetail
from openziti_edge_management.model.posture_check_domain_create import PostureCheckDomainCreate
from openziti_edge_management.model.posture_check_domain_create_all_of import PostureCheckDomainCreateAllOf
from openziti_edge_management.model.posture_check_domain_detail import PostureCheckDomainDetail
from openziti_edge_management.model.posture_check_domain_patch import PostureCheckDomainPatch
from openziti_edge_management.model.posture_check_domain_patch_all_of import PostureCheckDomainPatchAllOf
from openziti_edge_management.model.posture_check_domain_update import PostureCheckDomainUpdate
from openziti_edge_management.model.posture_check_failure import PostureCheckFailure
from openziti_edge_management.model.posture_check_failure_domain import PostureCheckFailureDomain
from openziti_edge_management.model.posture_check_failure_domain_all_of import PostureCheckFailureDomainAllOf
from openziti_edge_management.model.posture_check_failure_mac_address import PostureCheckFailureMacAddress
from openziti_edge_management.model.posture_check_failure_mac_address_all_of import PostureCheckFailureMacAddressAllOf
from openziti_edge_management.model.posture_check_failure_mfa import PostureCheckFailureMfa
from openziti_edge_management.model.posture_check_failure_mfa_all_of import PostureCheckFailureMfaAllOf
from openziti_edge_management.model.posture_check_failure_operating_system import PostureCheckFailureOperatingSystem
from openziti_edge_management.model.posture_check_failure_operating_system_actual import PostureCheckFailureOperatingSystemActual
from openziti_edge_management.model.posture_check_failure_operating_system_all_of import PostureCheckFailureOperatingSystemAllOf
from openziti_edge_management.model.posture_check_failure_process import PostureCheckFailureProcess
from openziti_edge_management.model.posture_check_failure_process_actual import PostureCheckFailureProcessActual
from openziti_edge_management.model.posture_check_failure_process_all_of import PostureCheckFailureProcessAllOf
from openziti_edge_management.model.posture_check_failure_process_multi import PostureCheckFailureProcessMulti
from openziti_edge_management.model.posture_check_failure_process_multi_all_of import PostureCheckFailureProcessMultiAllOf
from openziti_edge_management.model.posture_check_mac_address_create import PostureCheckMacAddressCreate
from openziti_edge_management.model.posture_check_mac_address_create_all_of import PostureCheckMacAddressCreateAllOf
from openziti_edge_management.model.posture_check_mac_address_detail import PostureCheckMacAddressDetail
from openziti_edge_management.model.posture_check_mac_address_patch import PostureCheckMacAddressPatch
from openziti_edge_management.model.posture_check_mac_address_patch_all_of import PostureCheckMacAddressPatchAllOf
from openziti_edge_management.model.posture_check_mac_address_update import PostureCheckMacAddressUpdate
from openziti_edge_management.model.posture_check_mfa_create import PostureCheckMfaCreate
from openziti_edge_management.model.posture_check_mfa_detail import PostureCheckMfaDetail
from openziti_edge_management.model.posture_check_mfa_patch import PostureCheckMfaPatch
from openziti_edge_management.model.posture_check_mfa_properties import PostureCheckMfaProperties
from openziti_edge_management.model.posture_check_mfa_properties_patch import PostureCheckMfaPropertiesPatch
from openziti_edge_management.model.posture_check_mfa_update import PostureCheckMfaUpdate
from openziti_edge_management.model.posture_check_operating_system_create import PostureCheckOperatingSystemCreate
from openziti_edge_management.model.posture_check_operating_system_create_all_of import PostureCheckOperatingSystemCreateAllOf
from openziti_edge_management.model.posture_check_operating_system_detail import PostureCheckOperatingSystemDetail
from openziti_edge_management.model.posture_check_operating_system_detail_all_of import PostureCheckOperatingSystemDetailAllOf
from openziti_edge_management.model.posture_check_operating_system_patch import PostureCheckOperatingSystemPatch
from openziti_edge_management.model.posture_check_operating_system_patch_all_of import PostureCheckOperatingSystemPatchAllOf
from openziti_edge_management.model.posture_check_operating_system_update import PostureCheckOperatingSystemUpdate
from openziti_edge_management.model.posture_check_patch import PostureCheckPatch
from openziti_edge_management.model.posture_check_process_create import PostureCheckProcessCreate
from openziti_edge_management.model.posture_check_process_create_all_of import PostureCheckProcessCreateAllOf
from openziti_edge_management.model.posture_check_process_detail import PostureCheckProcessDetail
from openziti_edge_management.model.posture_check_process_multi_create import PostureCheckProcessMultiCreate
from openziti_edge_management.model.posture_check_process_multi_create_all_of import PostureCheckProcessMultiCreateAllOf
from openziti_edge_management.model.posture_check_process_multi_detail import PostureCheckProcessMultiDetail
from openziti_edge_management.model.posture_check_process_multi_patch import PostureCheckProcessMultiPatch
from openziti_edge_management.model.posture_check_process_multi_patch_all_of import PostureCheckProcessMultiPatchAllOf
from openziti_edge_management.model.posture_check_process_multi_update import PostureCheckProcessMultiUpdate
from openziti_edge_management.model.posture_check_process_patch import PostureCheckProcessPatch
from openziti_edge_management.model.posture_check_process_patch_all_of import PostureCheckProcessPatchAllOf
from openziti_edge_management.model.posture_check_process_update import PostureCheckProcessUpdate
from openziti_edge_management.model.posture_check_type import PostureCheckType
from openziti_edge_management.model.posture_check_type_detail import PostureCheckTypeDetail
from openziti_edge_management.model.posture_check_type_detail_all_of import PostureCheckTypeDetailAllOf
from openziti_edge_management.model.posture_check_type_list import PostureCheckTypeList
from openziti_edge_management.model.posture_check_update import PostureCheckUpdate
from openziti_edge_management.model.posture_checks_failure_mfa_criteria import PostureChecksFailureMfaCriteria
from openziti_edge_management.model.posture_checks_failure_mfa_values import PostureChecksFailureMfaValues
from openziti_edge_management.model.posture_data import PostureData
from openziti_edge_management.model.posture_data_base import PostureDataBase
from openziti_edge_management.model.posture_data_domain import PostureDataDomain
from openziti_edge_management.model.posture_data_domain_all_of import PostureDataDomainAllOf
from openziti_edge_management.model.posture_data_endpoint_state import PostureDataEndpointState
from openziti_edge_management.model.posture_data_envelope import PostureDataEnvelope
from openziti_edge_management.model.posture_data_mac import PostureDataMac
from openziti_edge_management.model.posture_data_mac_all_of import PostureDataMacAllOf
from openziti_edge_management.model.posture_data_mfa import PostureDataMfa
from openziti_edge_management.model.posture_data_os import PostureDataOs
from openziti_edge_management.model.posture_data_os_all_of import PostureDataOsAllOf
from openziti_edge_management.model.posture_data_process import PostureDataProcess
from openziti_edge_management.model.posture_data_process_all_of import PostureDataProcessAllOf
from openziti_edge_management.model.posture_queries import PostureQueries
from openziti_edge_management.model.posture_query import PostureQuery
from openziti_edge_management.model.posture_query_all_of import PostureQueryAllOf
from openziti_edge_management.model.posture_query_process import PostureQueryProcess
from openziti_edge_management.model.process import Process
from openziti_edge_management.model.process_multi import ProcessMulti
from openziti_edge_management.model.re_enroll import ReEnroll
from openziti_edge_management.model.role_attributes_list import RoleAttributesList
from openziti_edge_management.model.roles import Roles
from openziti_edge_management.model.router_create import RouterCreate
from openziti_edge_management.model.router_detail import RouterDetail
from openziti_edge_management.model.router_detail_all_of import RouterDetailAllOf
from openziti_edge_management.model.router_entity_ref import RouterEntityRef
from openziti_edge_management.model.router_entity_ref_all_of import RouterEntityRefAllOf
from openziti_edge_management.model.router_list import RouterList
from openziti_edge_management.model.router_patch import RouterPatch
from openziti_edge_management.model.router_update import RouterUpdate
from openziti_edge_management.model.sdk_info import SdkInfo
from openziti_edge_management.model.semantic import Semantic
from openziti_edge_management.model.service_config_assign import ServiceConfigAssign
from openziti_edge_management.model.service_config_detail import ServiceConfigDetail
from openziti_edge_management.model.service_config_list import ServiceConfigList
from openziti_edge_management.model.service_configs_assign_list import ServiceConfigsAssignList
from openziti_edge_management.model.service_create import ServiceCreate
from openziti_edge_management.model.service_detail import ServiceDetail
from openziti_edge_management.model.service_detail_all_of import ServiceDetailAllOf
from openziti_edge_management.model.service_edge_router_policy_create import ServiceEdgeRouterPolicyCreate
from openziti_edge_management.model.service_edge_router_policy_detail import ServiceEdgeRouterPolicyDetail
from openziti_edge_management.model.service_edge_router_policy_detail_all_of import ServiceEdgeRouterPolicyDetailAllOf
from openziti_edge_management.model.service_edge_router_policy_list import ServiceEdgeRouterPolicyList
from openziti_edge_management.model.service_edge_router_policy_patch import ServiceEdgeRouterPolicyPatch
from openziti_edge_management.model.service_edge_router_policy_update import ServiceEdgeRouterPolicyUpdate
from openziti_edge_management.model.service_list import ServiceList
from openziti_edge_management.model.service_patch import ServicePatch
from openziti_edge_management.model.service_policy_create import ServicePolicyCreate
from openziti_edge_management.model.service_policy_detail import ServicePolicyDetail
from openziti_edge_management.model.service_policy_detail_all_of import ServicePolicyDetailAllOf
from openziti_edge_management.model.service_policy_list import ServicePolicyList
from openziti_edge_management.model.service_policy_patch import ServicePolicyPatch
from openziti_edge_management.model.service_policy_update import ServicePolicyUpdate
from openziti_edge_management.model.service_update import ServiceUpdate
from openziti_edge_management.model.session_detail import SessionDetail
from openziti_edge_management.model.session_detail_all_of import SessionDetailAllOf
from openziti_edge_management.model.session_edge_router import SessionEdgeRouter
from openziti_edge_management.model.session_edge_router_all_of import SessionEdgeRouterAllOf
from openziti_edge_management.model.session_management_detail import SessionManagementDetail
from openziti_edge_management.model.session_management_detail_all_of import SessionManagementDetailAllOf
from openziti_edge_management.model.session_management_list import SessionManagementList
from openziti_edge_management.model.session_route_path_detail import SessionRoutePathDetail
from openziti_edge_management.model.spec_detail import SpecDetail
from openziti_edge_management.model.spec_detail_all_of import SpecDetailAllOf
from openziti_edge_management.model.spec_list import SpecList
from openziti_edge_management.model.sub_tags import SubTags
from openziti_edge_management.model.tags import Tags
from openziti_edge_management.model.terminator_cost import TerminatorCost
from openziti_edge_management.model.terminator_cost_map import TerminatorCostMap
from openziti_edge_management.model.terminator_create import TerminatorCreate
from openziti_edge_management.model.terminator_detail import TerminatorDetail
from openziti_edge_management.model.terminator_detail_all_of import TerminatorDetailAllOf
from openziti_edge_management.model.terminator_list import TerminatorList
from openziti_edge_management.model.terminator_patch import TerminatorPatch
from openziti_edge_management.model.terminator_precedence import TerminatorPrecedence
from openziti_edge_management.model.terminator_precedence_map import TerminatorPrecedenceMap
from openziti_edge_management.model.terminator_update import TerminatorUpdate
from openziti_edge_management.model.trace_detail import TraceDetail
from openziti_edge_management.model.trace_detail_envelope import TraceDetailEnvelope
from openziti_edge_management.model.trace_spec import TraceSpec
from openziti_edge_management.model.username import Username
from openziti_edge_management.model.username_nullable import UsernameNullable
from openziti_edge_management.model.version import Version
from openziti_edge_management.model.version_info import VersionInfo
