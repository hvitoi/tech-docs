# %%
import uuid

# the uuidv5 is designed use as a seed a namespace (another uuid) and a string
# deterministic: same seed + same name → same UUID, always

namespace = uuid.UUID("12345678-1234-5678-1234-567812345678")
uuid.uuid5(namespace, "user-42")

# %%
# When you just want an UUID based on a string and you don't have a "strong"namespace, you should:
# Create your own namespace! With what your application needs to hold an uuid constant
# Or, if you don't mind about collisions, use NAMESPACE_OID

uuid.uuid5(uuid.NAMESPACE_OID, "abc")

# %%
# These namespaces are constant defined in the UUID spec itself — RFC 4122 Appendix C (now RFC 9562)
uuid.uuid5(uuid.NAMESPACE_DNS, "abc")  # for hostnames
uuid.uuid5(uuid.NAMESPACE_URL, "abc")  # for URLs
uuid.uuid5(uuid.NAMESPACE_OID, "abc")  # for ISO OIDs
uuid.uuid5(uuid.NAMESPACE_X500, "abc")  # for X.500 DNs
