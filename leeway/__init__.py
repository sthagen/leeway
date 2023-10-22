# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.25b2f774'
# [[[end]]] (checksum: af4497b40adbd7cbf7116732d6106bcd)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
