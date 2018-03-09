from insights.core.spec_factory import first_file, first_of, glob_file, simple_file
from functools import partial
from insights.core.context import HostArchiveContext
from insights.specs import Specs

simple_file = partial(simple_file, context=HostArchiveContext)
glob_file = partial(glob_file, context=HostArchiveContext)


class InsightsArchiveSpecs(Specs):

    blkid = simple_file("insights_commands/blkid_-c_.dev.null")
    brctl_show = simple_file("insights_commands/brctl_show")
    ceph_df_detail = simple_file("insights_commands/ceph_df_detail_-f_json-pretty")
    ceph_health_detail = simple_file("insights_commands/ceph_health_detail_-f_json-pretty")
    ceph_osd_df = simple_file("insights_commands/ceph_osd_df_-f_json-pretty")
    ceph_osd_dump = simple_file("insights_commands/ceph_osd_dump_-f_json-pretty")
    ceph_osd_ec_profile_ls = simple_file("insights_commands/ceph_osd_erasure-code-profile_ls")
    ceph_osd_tree = simple_file("insights_commands/ceph_osd_tree_-f_json-pretty")
    ceph_s = simple_file("insights_commands/ceph_-s_-f_json-pretty")
    ceph_v = simple_file("insights_commands/ceph_-v")
    certificates_enddate = simple_file("insights_commands/find_.etc.origin.node_.etc.origin.master_.etc.pki_-type_f_-exec_.usr.bin.openssl_x509_-noout_-enddate_-in_-exec_echo_FileName")
    chkconfig = simple_file("insights_commands/chkconfig_--list")
    chronyc_sources = simple_file("insights_commands/chronyc_sources")
    crt = simple_file("insights_commands/find_.etc.origin.node_.etc.origin.master_-type_f_-path_.crt")
    date = simple_file("insights_commands/date")
    date_iso = simple_file("insights_commands/date_--iso-8601_seconds")
    date_utc = simple_file("insights_commands/date_--utc")
    df__al = simple_file("insights_commands/df_-al")
    df__alP = simple_file("insights_commands/df_-alP")
    df__li = simple_file("insights_commands/df_-li")
    dig = simple_file("insights_commands/dig_dnssec_._DNSKEY")
    dig_dnssec = simple_file("insights_commands/dig_dnssec_._SOA")
    dig_edns = simple_file("insights_commands/dig_edns_0_._SOA")
    dig_noedns = simple_file("insights_commands/dig_noedns_._SOA")
    display_java = simple_file("insights_commands/alternatives_--display_java")
    dmesg = simple_file("insights_commands/dmesg")
    dmidecode = simple_file("insights_commands/dmidecode")
    docker_info = simple_file("insights_commands/docker_info")
    docker_list_containers = simple_file("insights_commands/docker_ps_--all_--no-trunc")
    docker_list_images = simple_file("insights_commands/docker_images_--all_--no-trunc_--digests")
    dumpdev = simple_file("insights_commands/awk_.ext_234_._print_1_.proc.mounts")
    ethtool = glob_file("insights_commands/ethtool_*", ignore="ethtool_-.*")
    ethtool_S = glob_file("insights_commands/ethtool_-S_*")
    ethtool_a = glob_file("insights_commands/ethtool_-a_*")
    ethtool_c = glob_file("insights_commands/ethtool_-c_*")
    ethtool_g = glob_file("insights_commands/ethtool_-g_*")
    ethtool_i = glob_file("insights_commands/ethtool_-i_*")
    ethtool_k = glob_file("insights_commands/ethtool_-k_*")
    facter = simple_file("insights_commands/facter")
    fc_match = simple_file("insights_commands/fc-match_-sv_sans_regular_roman_family_fontformat")
    fdisk_l = simple_file("insights_commands/fdisk_-l")
    foreman_rake_db_migrate_status = simple_file('insights_commands/foreman-rake_db_migrate_status')
    getenforce = simple_file("insights_commands/getenforce")
    getsebool = simple_file("insights_commands/getsebool_-a")
    grub1_config_perms = simple_file("insights_commands/ls_-l_.boot.grub.grub.conf")
    grub_config_perms = simple_file("insights_commands/ls_-l_.boot.grub2.grub.cfg")
    hammer_ping = simple_file("insights_commands/hammer_ping")
    hammer_task_list = simple_file("insights_commands/hammer_--csv_task_list")
    heat_crontab = simple_file("insights_commands/crontab_-l_-u_heat")
    # simple_file("insights_commands/rpm_-qa_--qf_NAME_-_VERSION_-_RELEASE_._ARCH_INSTALLTIME_date_BUILDTIME_RSAHEADER_pgpsig_DSAHEADER_pgpsig")])
    installed_rpms = first_file([
        "insights_commands/rpm_-qa_--qf_NAME_-_VERSION_-_RELEASE_._ARCH_INSTALLTIME_date_BUILDTIME_VENDOR_BUILDHOST_DUMMY_SIGPGP_pgpsig",
        "insights_commands/rpm_-qa_--qf_NAME_-_VERSION_-_RELEASE_._ARCH_INSTALLTIME_date_BUILDTIME_RSAHEADER_pgpsig_DSAHEADER_pgpsig"
    ])
    hostname = first_of([simple_file("insights_commands/hostname_-f"), simple_file("insights_commands/hostname")])
    hponcfg_g = simple_file("insights_commands/hponcfg_-g")
    httpd_pid = simple_file("insights_commands/pgrep_-o_httpd")
    ifconfig = simple_file("insights_commands/ifconfig_-a")
    ip6tables = simple_file("insights_commands/ip6tables-save")
    ip_addr = simple_file("insights_commands/ip_addr")
    ip_route_show_table_all = simple_file("insights_commands/ip_route_show_table_all")
    ip_s_link = simple_file("insights_commands/ip_-s_link")
    ipcs_s = simple_file("insights_commands/ipcs_-s")
    iptables = simple_file("insights_commands/iptables-save")
    ipv4_neigh = simple_file("insights_commands/ip_-4_neighbor_show_nud_all")
    ipv6_neigh = simple_file("insights_commands/ip_-6_neighbor_show_nud_all")
    iscsiadm_m_session = simple_file("insights_commands/iscsiadm_-m_session")
    katello_service_status = simple_file("insights_commands/katello-service_status")
    keystone_crontab = simple_file("insights_commands/crontab_-l_-u_keystone")
    libkeyutils = simple_file("insights_commands/find_-L_.lib_.lib64_-name_libkeyutils.so")
    libkeyutils_objdumps = simple_file("insights_commands/find_-L_.lib_.lib64_-name_libkeyutils.so.1_-exec_objdump_-x")
    locale = simple_file("insights_commands/locale")
    localtime = simple_file("insights_commands/file_-L_.etc.localtime")
    lpstat_p = simple_file("insights_commands/lpstat_-p")
    ls_boot = simple_file("insights_commands/ls_-lanR_.boot")
    ls_dev = simple_file("insights_commands/ls_-lanR_.dev")
    ls_disk = simple_file("insights_commands/ls_-lanR_.dev.disk")
    ls_docker_volumes = simple_file("insights_commands/ls_-lanR_.var.lib.docker.volumes")
    ls_etc = simple_file("insights_commands/ls_-lanR_.etc")
    ls_sys_firmware = simple_file("insights_commands/ls_-lanR_.sys.firmware")
    ls_var_log = simple_file("insights_commands/ls_-la_.var.log_.var.log.audit")
    ls_var_www = simple_file("insights_commands/ls_-la_.dev.null_.var.www")
    lsblk = simple_file("insights_commands/lsblk")
    lsblk_pairs = simple_file("insights_commands/lsblk_-P_-o_NAME_KNAME_MAJ_MIN_FSTYPE_MOUNTPOINT_LABEL_UUID_RA_RO_RM_MODEL_SIZE_STATE_OWNER_GROUP_MODE_ALIGNMENT_MIN-IO_OPT-IO_PHY-SEC_LOG-SEC_ROTA_SCHED_RQ-SIZE_TYPE_DISC-ALN_DISC-GRAN_DISC-MAX_DISC-ZERO")
    lscpu = simple_file("insights_commands/lscpu")
    lsmod = simple_file("insights_commands/lsmod")
    lsof = simple_file("insights_commands/lsof")
    lspci = simple_file("insights_commands/lspci")
    lssap = simple_file("insights_commands/usr.sap.hostctrl.exe.lssap")
    lvdisplay = simple_file("insights_commands/lvdisplay")
    lvs_noheadings = simple_file("insights_commands/lvs_--nameprefixes_--noheadings_--separator_-a_-o_lv_name_lv_size_lv_attr_mirror_log_vg_name_devices_region_size_data_percent_metadata_percent_--config_global_locking_type_0")
    lvs_noheadings_all = simple_file("insights_commands/lvs_--nameprefixes_--noheadings_--separator_-a_-o_lv_name_lv_size_lv_attr_mirror_log_vg_name_devices_region_size_data_percent_metadata_percent_--config_global_locking_type_0_devices_filter_a")
    md5chk_files = simple_file("insights_commands/ls_-H_.usr.lib_._libfreeblpriv3.so_libsoftokn3.so_.etc.pki.product_.69.pem_.etc.fonts.fonts.conf_.dev.null_2_.dev.null")
    mlx4_port = simple_file("insights_commands/find_.sys.bus.pci.devices._.mlx4_port_0-9_-print_-exec_cat")
    mount = simple_file("insights_commands/mount")
    multicast_querier = simple_file("insights_commands/find_.sys.devices.virtual.net._-name_multicast_querier_-print_-exec_cat")
    multipath__v4__ll = simple_file("insights_commands/multipath_-v4_-ll")
    named_checkconf_p = simple_file("insights_commands/named-checkconf_-p")
    netstat = simple_file("insights_commands/netstat_-neopa")
    netstat_agn = simple_file("insights_commands/netstat_-agn")
    netstat_i = simple_file("insights_commands/netstat_-i")
    netstat_s = simple_file("insights_commands/netstat_-s")
    nmcli_dev_show = simple_file("insights_commands/nmcli_dev_show")
    nova_crontab = simple_file("insights_commands/crontab_-l_-u_nova")
    ntpq_leap = simple_file("insights_commands/ntpq_-c_rv_0_leap")
    ntpq_pn = simple_file("insights_commands/ntpq_-pn")
    ntptime = simple_file("insights_commands/ntptime")
    numeric_user_group_name = simple_file("insights_commands/grep_-c_digit_.etc.passwd_.etc.group")
    oc_get_bc = simple_file("insights_commands/oc_get_bc_-o_yaml_--all-namespaces")
    oc_get_dc = simple_file("insights_commands/oc_get_dc_-o_yaml_--all-namespaces")
    oc_get_egressnetworkpolicy = simple_file("insights_commands/oc_get_egressnetworkpolicy_-o_yaml_--all-namespaces")
    oc_get_endpoints = simple_file("insights_commands/oc_get_endpoints_-o_yaml_--all-namespaces")
    oc_get_event = simple_file("insights_commands/oc_get_event_-o_yaml_--all-namespaces")
    oc_get_node = simple_file("insights_commands/oc_get_nodes_-o_yaml")
    oc_get_pod = simple_file("insights_commands/oc_get_pod_-o_yaml_--all-namespaces")
    oc_get_project = simple_file("insights_commands/oc_get_project_-o_yaml_--all-namespaces")
    oc_get_pv = simple_file("insights_commands/oc_get_pv_-o_yaml_--all-namespaces")
    oc_get_pvc = simple_file("insights_commands/oc_get_pvc_-o_yaml_--all-namespaces")
    oc_get_rc = simple_file("insights_commands/oc_get_rc_-o_yaml_--all-namespaces")
    oc_get_role = simple_file("insights_commands/oc_get_role_-o_yaml_--all-namespaces")
    oc_get_rolebinding = simple_file("insights_commands/oc_get_rolebinding_-o_yaml_--all-namespaces")
    oc_get_service = simple_file("insights_commands/oc_get_service_-o_yaml_--all-namespaces")
    openvswitch_other_config = simple_file("insights_commands/ovs-vsctl_-t_5_get_Open_vSwitch_._other_config")
    ovs_vsctl_show = simple_file("insights_commands/ovs-vsctl_show")
    parted__l = simple_file("insights_commands/parted_-l_-s")
    pcs_status = simple_file("insights_commands/pcs_status")
    ps_aux = simple_file("insights_commands/ps_aux")
    ps_auxcww = simple_file("insights_commands/ps_auxcww")
    ps_auxww = simple_file("insights_commands/ps_auxww")
    pvs = simple_file("insights_commands/pvs_-a_-v_-o_pv_mda_free_pv_mda_size_pv_mda_count_pv_mda_used_count_pe_count_--config_global_locking_type_0")
    pvs_noheadings = simple_file("insights_commands/pvs_--nameprefixes_--noheadings_--separator_-a_-o_pv_all_vg_name_--config_global_locking_type_0")
    pvs_noheadings_all = simple_file("insights_commands/pvs_--nameprefixes_--noheadings_--separator_-a_-o_pv_all_vg_name_--config_global_locking_type_0_devices_filter_a")
    qpid_stat_q = simple_file("insights_commands/qpid-stat_-q_--ssl-certificate_.etc.pki.katello.qpid_client_striped.crt_-b_amqps_..localhost_5671")
    qpid_stat_u = simple_file("insights_commands/qpid-stat_-u_--ssl-certificate_.etc.pki.katello.qpid_client_striped.crt_-b_amqps_..localhost_5671")
    rabbitmq_policies = simple_file("insights_commands/rabbitmqctl_list_policies")
    rabbitmq_queues = simple_file("insights_commands/rabbitmqctl_list_queues_name_messages_consumers_auto_delete")
    rabbitmq_report = simple_file("insights_commands/rabbitmqctl_report")
    rabbitmq_users = simple_file("insights_commands/rabbitmqctl_list_users")
    rhn_charsets = simple_file("insights_commands/rhn-charsets")
    rhn_schema_stats = simple_file("insights_commands/rhn-schema-stats")
    rhn_schema_version = simple_file("insights_commands/rhn-schema-version")
    root_crontab = simple_file("insights_commands/crontab_-l_-u_root")
    route = simple_file("insights_commands/route_-n")
    rpm_V_packages = simple_file("insights_commands/rpm_-V_coreutils_procps_procps-ng_shadow-utils_passwd_sudo")
    saphostctl_getcimobject_sapinstance = simple_file("insights_commands/saphostctrl_-function_GetCIMObject_-enuminstances_SAPInstance")
    sestatus = simple_file("insights_commands/sestatus_-b")
    smbstatus_S = simple_file("insights_commands/smbstatus_-S")
    smbstatus_p = simple_file("insights_commands/smbstatus_-p")
    ss = simple_file("insights_commands/ss_-tulpn")
    sshd_config_perms = simple_file("insights_commands/ls_-l_.etc.ssh.sshd_config")
    subscription_manager_list_consumed = simple_file('insights_commands/subscription-manager_list_--consumed')
    subscription_manager_list_installed = simple_file('insights_commands/subscription-manager_list_--installed')
    sysctl = simple_file("insights_commands/sysctl_-a")
    sysctl_conf_initramfs = simple_file("insights_commands/lsinitrd_.boot.initramfs-_kdump.img_-f_.etc.sysctl.conf_.etc.sysctl.d._.conf")
    systemctl_cinder_volume = simple_file("insights_commands/systemctl_show_openstack-cinder-volume")
    systemctl_list_unit_files = simple_file("insights_commands/systemctl_list-unit-files")
    systemctl_list_units = simple_file("insights_commands/systemctl_list-units")
    systemctl_mariadb = simple_file("insights_commands/systemctl_show_mariadb")
    systemctl_pulp_workers = simple_file("insights_commands/systemctl_show_pulp_workers")
    systemctl_pulp_resmg = simple_file("insights_commands/systemctl_show_pulp_resource_manager")
    systemctl_pulp_celerybeat = simple_file("insights_commands/systemctl_show_pulp_celerybeat")
    tomcat_vdc_fallback = simple_file("insights_commands/find_.usr.share_-maxdepth_1_-name_tomcat_-exec_.bin.grep_-R_-s_VirtualDirContext_--include_.xml")
    tuned_adm = simple_file("insights_commands/tuned-adm_list")
    uname = simple_file("insights_commands/uname_-a")
    uptime = simple_file("insights_commands/uptime")
    vgdisplay = simple_file("insights_commands/vgdisplay")
    vgs_noheadings = simple_file("insights_commands/vgs_--nameprefixes_--noheadings_--separator_-a_-o_vg_all_--config_global_locking_type_0")
    vgs_noheadings_all = simple_file("insights_commands/vgs_--nameprefixes_--noheadings_--separator_-a_-o_vg_all_--config_global_locking_type_0_devices_filter_a")
    virt_what = simple_file("insights_commands/virt-what")
    woopsie = simple_file("insights_commands/find_.var.crash_.var.tmp_-path_.reports-_.whoopsie-report")
    yum_repolist = simple_file("insights_commands/yum_-C_repolist")
