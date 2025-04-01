import os

from Project import Project
from Version import Version


def isProjectVersioned(project: Project):
    head = project.getHead()
    projectDirectory = project.projectDirectory
    ignorePatterns = project.getIgnorePatterns()

    localVersion = Version(['Placeholder'],'placeholder', project)
    localVersion.addElementsFromDirectory(projectDirectory, ignorePatterns)

    headVersion = Version(['Placeholder'],'placeholder', project)
    headVersionFile = os.path.join(project.versionsDirectory, head)
    headVersion.addElementsFromVersionFile(headVersionFile)

    return localVersion.elements == headVersion.elements

def getVersionFromHash(hash, project):
    versions = project.getVersions()
    version = [ver for ver in versions if ver.hash == hash]
    return(version[0])


def find_closest_common_ancestors(version1, version2, project):
    def get_ancestors(version):
        ancestors = []
        visited = set()
        queue = [(version, 0)]  # (version, depth)
        depth_map = {}  # Store depth of each version
        
        while queue:
            current_version, depth = queue.pop(0)
            if current_version.hash in visited:
                continue
            visited.add(current_version.hash)
            ancestors.append((current_version, depth))
            depth_map[current_version.hash] = depth
            
            for ancestor_hash in current_version.ancestors:
                queue.append((getVersionFromHash(ancestor_hash, project), depth + 1))
        
        return ancestors, depth_map
    
    ancestors_v1, depth_v1 = get_ancestors(version1)
    ancestors_v2, depth_v2 = get_ancestors(version2)
    
    common_ancestors = []
    min_depth = float('inf')
    
    ancestors_v1_hashes = {v.hash for v, _ in ancestors_v1}
    for v, depth in ancestors_v2:
        if v.hash in ancestors_v1_hashes:
            common_depth = max(depth, depth_v1[v.hash])
            if common_depth < min_depth:
                min_depth = common_depth
                common_ancestors = [v]
            elif common_depth == min_depth:
                common_ancestors.append(v)
    
    return common_ancestors



# def getAncestorsof2(A,B):
#     return ANCESTORS

# def merge2versions(A, B, COMMON):
#     return MERGED

# def mergeVersions(versions):


#     C = versions.pop()

#     while len(versions) > 1:
#         D = versions.pop()
#         ANCESTORS = getAncestorsof2(C,D)
#         COMMON = mergeVersions(ANCESTORS)

#         C = merge2versions(C,D, COMMON)
    
#     return C


    