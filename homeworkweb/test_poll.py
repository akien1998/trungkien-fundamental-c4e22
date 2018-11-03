from poll import River
import mlap
mlap.connect()

river= River.objects()
for p in river:
    if p.continent =="Africa":
        print(p.name)
        print(p.continent)
        print(p.length)
        print("===============")