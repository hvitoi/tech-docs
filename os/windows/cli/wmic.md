# wmic

```powershell
wmic path softwareLicensingService get OA3xOriginalProductKey
```

```powershell
(Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey
```
