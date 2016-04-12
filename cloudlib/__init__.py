import sys
import pkg_resources

# If there is a conflicting non egg module,
# i.e. an older standard system module installed,
# then replace it with this requirement
def replace_dist(requirement):
    try:
        return pkg_resources.require(requirement)
    except pkg_resources.VersionConflict:
        e = sys.exc_info()[1]
        dist=e.args[0]
        req=e.args[1]
        if dist.key == req.key and not dist.location.endswith('.egg'):
            del pkg_resources.working_set.by_key[dist.key]
            # We assume there is no need to adjust sys.path
            # and the associated pkg_resources.working_set.entries
            return pkg_resources.require(requirement)

replace_dist("WebOb >= 1.0")

replace_dist("PasteDeploy >= 1.5.0")
# This hack is needed because replace_dist() results in
# the standard paste module path being at the start of __path__.
# TODO: See can we get pkg_resources to do the right thing directly
import paste
paste.__path__.insert(0, paste.__path__.pop(-1))

