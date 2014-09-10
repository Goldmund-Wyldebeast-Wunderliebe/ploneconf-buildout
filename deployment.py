from base.deployment import (_modules, get_dvl, get_tst, get_acc,
    get_prd, get_prdbe, get_prdfe, templates)

_base_port = 8210
_env_name = 'hhd'
_site_id = 'hhd_intranet'

_modules.update({
    'hhd.theme.intranet': 'git git@git.gw20e.com:waterschappen/hhd-theme-intranet.git',
    'hhd.theme.internet': 'git git@git.gw20e.com:waterschappen/hhd-theme-internet.git',
})

dvl = get_dvl(_base_port, _env_name, _site_id)
tst = get_tst(_base_port, _env_name, _site_id)
acc = get_acc(_base_port, _env_name, _site_id)
prd = get_prd(_base_port, _env_name, _site_id)
prdbe = get_prdbe(_base_port, _env_name, prd)
prdfe = get_prdfe(_base_port, _env_name, prd)


default = 'tst'
