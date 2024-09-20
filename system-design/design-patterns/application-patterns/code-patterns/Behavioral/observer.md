# Observer

- Push-based system
- Allow many objects to subscribe to events (one-to-many)
- Callback functions are triggered whenever a new message is received

```typescript
import { Subject } from "rxjs";

const news = new Subject();

const tv1 = news.subscribe((v) => console.log(v + "via Den TV"));
const tv2 = news.subscribe((v) => console.log(v + "via Batcave TV"));
const tv3 = news.subscribe((v) => console.log(v + "via Airport TV"));

news.next("Breaking news: ");
news.next("The war is over ");

tv1.unsubscribe();
```
