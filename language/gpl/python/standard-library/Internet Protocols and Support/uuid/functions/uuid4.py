# %%
# UUID v4 is supposed to be unpredictable
# uuid.uuid4() reads from os.urandom() -  a cryptographically secure source
# If the UUID uses another seeder (e.g., random.Random), an attack can observe a few public UUIDs (e.g. from URLs, public API responses, leaked logs), recover the PRNG state and predict next UUID

import uuid

uuid.uuid4()
