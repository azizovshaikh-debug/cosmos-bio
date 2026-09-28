import qrcode

base = "https://azizovshaikh-debug.github.io/cosmos-bio/"

pages = {
    "index": "Главная",
    "stick-insects": "Палочники",
    "snails": "Улитки",
    "cockroaches": "Тараканы",
    "lettuce": "Салат",
    "fruit-flies": "Дрозофилы",
    "wheat": "Пшеница",
    "zinnia": "Цинния",
}

for name, title in pages.items():
    url = base if name == "index" else base + name + ".html"
    img = qrcode.make(url)
    filename = f"qr_{name}.png"
    img.save(filename)
    print(f"✅ {title}: {url}")