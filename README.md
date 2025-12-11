# WebApp - Prijavnica Management System

## 📋 Pregled Projekta

WebApp je Django aplikacija za upravljanje prijavnic z avtomatiziranim testiranjem in CI/CD pipeline-om.

### Glavne Lastnosti
- 👥 User authentication in authorization
- 📝 Prijavnica management (CRUD operacije)
- 📊 KPI dashboard za analytics
- 🔐 Admin in user roles
- ✅ 30+ avtomatiziranih testov
- 🚀 GitHub Actions CI/CD pipeline

## 📁 Struktura Projekta

```
attempt3ip/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── package.json
├── jest.config.js
├── .babelrc
├── ip_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── webapp/
│   ├── models.py          # Prijavnica model
│   ├── views.py           # View logika
│   ├── forms.py           # Django forme
│   ├── test_models.py     # 10 model testov
│   ├── test_views.py      # 9 view testov
│   ├── test_forms.py      # 4 form testov
│   ├── test_integrations.py # 9 integration testov
│   ├── static/
│   │   └── js/
│   │       ├── utils.js        # Frontend utility funkcije
│   │       └── utils.test.js   # 23 Jest testov
│   └── templates/
└── .github/
    └── workflows/
        └── ci-cd.yml       # GitHub Actions workflow
```

## 🚀 Quick Start

### Zahteve
- Python 3.9+
- Node.js 18+
- Django 4.1+

### Setup

```bash
# Backend
cd attempt3ip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

# Frontend
npm install
```

### Zagon Aplikacije

```bash
cd attempt3ip
python manage.py runserver
```

Aplikacija bo dostopna na `http://localhost:8000/`

## ✅ Testiranje

### Lokalno

```bash
# Backend testi
cd attempt3ip
python manage.py test webapp

# S coverage poročilom
coverage run --source='webapp' manage.py test webapp
coverage report
```

```bash
# Frontend testi
cd attempt3ip
npm test

# S coverage poročilom
npm test -- --coverage
```

### GitHub Actions

Testi se samodejno izvršijo pri:
- Push na `main` ali `develop` branch
- Pull request na `main` ali `develop` branch

Coverage poročila so dostopna v "Actions" tabuli.

## 📊 Test Coverage

### Backend Tests (21 testov)

**test_models.py (10 testov)**
- Kreiranje prijavnice
- String reprezentacija
- Field validacija
- Default vrednosti
- User relationships
- Multiple prijavnice na user

**test_views.py (9 testov)**
- Login (valid/invalid)
- Home view (staff/regular user)
- Prijavnice listing
- KPI calculations
- Permissions

**test_integrations.py (9 testov)**
- User edit flow
- Admin edit flow
- Prijavnica creation
- Authorization checks

### Frontend Tests (23 testov)

**utils.test.js (23 testov)**
- Chart data validation (5 testov)
- Percentage calculations (6 testov)
- Email validation (8 testov)
- Phone validation (7 testov)
- Integration scenarios (2 testa)

## 🔄 GitHub Actions Pipeline

### Jobs

1. **backend-tests** - Django testi na Python 3.9, 3.10, 3.11
2. **frontend-tests** - Jest testi na Node.js 18
3. **coverage-report** - Kombinira coverage poročila
4. **test-summary** - Prikazuje povzetek rezultatov

### Artefakti

Generirana poročila so shranjena kot GitHub Actions artifacts:
- `backend-coverage-reports-pyX.Y/` - Django coverage
- `frontend-coverage-reports/` - Jest coverage
- `combined-coverage-reports/` - Kombinirana poročila

Artefakti so dostopni 30-60 dni.

## 📖 Dokumentacija

- **TESTING.md** - Podrobna dokumentacija testov in CI/CD
- **denne smernice** - Django dokumentacija
- **Jest docs** - Frontend test dokumentacija

## 👥 User Roles

### Regular User
- Kreiranje lastnih prijavnic
- Uređivanje lastnih prijavnic
- Pregled lastne zgodovine

### Admin/Staff
- Pregled vseh prijavnic
- Validacija/zavrnitev prijavnic
- Dodajanje komentarjev
- Dostop do KPI dashboarda

## 🛠️ Tehnologije

### Backend
- Django 4.1
- Django ORM
- Coverage.py

### Frontend
- JavaScript (ES6+)
- Jest
- Chart.js

### DevOps
- GitHub Actions
- Docker (pripravljeno)
- SQLite (development)

## 📝 Licenca

MIT License

## 📞 Support

Za vprašanja ali probleme, odprite GitHub issue.

---

**Status**: ✅ Production Ready  
**Last Updated**: December 2024  
**Test Coverage**: 30+ testov + GitHub Actions CI/CD
