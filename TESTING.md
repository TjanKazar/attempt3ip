# Testing & CI/CD Documentation

## Test Overview

Ta projekt ima celovit test suite s 20+ testi za backend in frontend ter avtomatizirani CI/CD pipeline.

### Struktura Testov

#### Backend Tests (Django)
**Lokacija**: `attempt3ip/webapp/test_*.py`

1. **test_models.py** - 9 testov za Prijavnica model
   - `test_prijavnica_creation` - Kreiranje nove prijavnice
   - `test_prijavnica_str_representation` - String reprezentacija
   - `test_prijavnica_phone_field` - Validacija phone polja
   - `test_prijavnica_dejavnost_field` - Validacija dejavnost polja
   - `test_prijavnica_valid_default_value` - Default vrednost valid polja
   - `test_prijavnica_valid_true` - Postavljanje valid na True
   - `test_prijavnica_valid_false` - Postavljanje valid na False
   - `test_prijavnica_komentar_field` - Validacija komentar polja
   - `test_prijavnica_user_relationship` - ForeignKey relacija
   - `test_multiple_prijavnice_per_user` - Več prijavnic na user

2. **test_views.py** - 9 testov za views
   - `test_login_page_GET` - Login stranica GET zahteva
   - `test_login_with_valid_credentials` - Login s pravilnimi kredenciali
   - `test_login_with_invalid_credentials` - Login s napačnimi kredenciali
   - `test_home_redirect_when_not_logged_in` - Zahteva redirect ko ni prijavljenega
   - `test_staff_user_sees_admin_home` - Admin vidi admin home
   - `test_regular_user_sees_user_home` - User vidi user home
   - `test_prijavnice_requires_login` - Zahteva login
   - `test_staff_can_view_all_prijavnice` - Admin vidi vse prijavnice
   - `test_regular_user_redirected_from_prijavnice` - User je preusmerjen
   - `test_kpi_view_GET` - KPI view GET zahteva
   - `test_kpi_counts_empty` - KPI counts ko ni podatkov
   - `test_kpi_counts_with_data` - KPI counts z podatki
   - `test_kpi_valid_percentage` - Izračun percentaze

3. **test_forms.py** - 4 testi za forme
   - `test_form_has_correct_fields` - Forma ima pravilna polja
   - `test_valid_form_submission` - Veljavna oddaja forme
   - `test_form_missing_required_field` - Forma brez obveznih polj
   - `test_form_saves_to_database` - Shranjevanje forme v bazo
   - `test_user_form_has_correct_fields` - User forma ima pravilna polja
   - `test_user_form_does_not_include_valid_and_komentar` - User forma nima točnih polj
   - `test_valid_user_form_submission` - Veljavna user forma
   - `test_user_form_update_prijavnica` - Posodabljanje prijavnice

#### Frontend Tests (Jest)
**Lokacija**: `attempt3ip/webapp/static/js/utils.test.js`

1. **Chart Validation Tests** - 5 testov
   - `validateChartData` - Validacija grafičnih podatkov
   - `getChartConfig` - Konfiguracija grafa

2. **Percentage Calculation Tests** - 6 testov
   - `formatValidationPercentage` - Oblikovanje percentaze

3. **Email Validation Tests** - 8 testov
   - `validateEmail` - Validacija e-poštnega naslova

4. **Phone Validation Tests** - 7 testov
   - `validatePhone` - Validacija telefonske številke

5. **Integration Tests** - 2 testa
   - Real-world data test
   - Form validation test

## Izvajanje Testov

### Backend Testi (lokalno)
```bash
cd attempt3ip
python manage.py test webapp
```

### Frontend Testi (lokalno)
```bash
cd attempt3ip
npm install
npm test
```

### S Coverage Poročilom
```bash
# Backend
cd attempt3ip
coverage run --source='webapp' manage.py test webapp
coverage report
coverage html

# Frontend
cd attempt3ip
npm test -- --coverage
```

## GitHub Actions CI/CD Pipeline

### Workflow Datoteka
**Lokacija**: `.github/workflows/ci-cd.yml`

### Jobs v Pipeline-u

1. **backend-tests**
   - Testira na Python verzijah: 3.9, 3.10, 3.11
   - Koraki:
     - Checkout code
     - Setup Python environment
     - Install dependencies
     - Run tests with coverage
     - Upload coverage reports
   - Artefakti: `backend-coverage-reports-pyX.Y`

2. **frontend-tests**
   - Testira na Node.js 18
   - Koraki:
     - Checkout code
     - Setup Node.js
     - Install dependencies
     - Run Jest tests with coverage
     - Upload coverage reports
   - Artefakti: `frontend-coverage-reports`

3. **coverage-report**
   - Kombinira coverage poročila iz backend in frontend
   - Koraki:
     - Download all coverage reports
     - Generate coverage summary
     - Upload combined reports
   - Artefakti: `combined-coverage-reports`

4. **test-summary**
   - Generirani povzetek vseh testov in rezultatov
   - Prikazuje status vseh jobs-ev

### Trigger Events
- `push` na `main` ali `develop` branch
- `pull_request` na `main` ali `develop` branch

### Artefakti

Vsi artefakti so dostopni v Actions tabula na GitHub-u in so hranjeni 30-60 dni.

#### Backend Coverage Artifacts
- `backend-coverage-reports-py3.9/coverage.xml`
- `backend-coverage-reports-py3.10/coverage.xml`
- `backend-coverage-reports-py3.11/coverage.xml`

#### Frontend Coverage Artifacts
- `frontend-coverage-reports/` - Kompleten Jest coverage direktorij

#### Combined Report
- `combined-coverage-reports/` - Vse coverage poročila v enem mestu

## Interpretacija Coverage Poročila

### Backend (Django/Coverage.py)
- **coverage.xml** - XML format za integracijo z drugimi tools-i
- **coverage report** - Tekstovni izpis pokritosti kode

### Frontend (Jest)
- **LCOV format** - Za integracijo z tools-i
- **JSON format** - Za progamski dostop
- **HTML report** (lokalno) - Vizuelni prikaz

## Test Quality Metrics

### Backend
- **20+ testov** za ključne komponente
- **Unit testi** za modele, forme in views
- **Integration testi** za login, navigation in data manipulation
- **Coverage** prikazuje procent pokrite kode

### Frontend
- **23+ testov** za utility funkcije
- **Validation testi** za email, telefon in grafikone
- **Integration testi** za real-world scenarije

## CI/CD Best Practices Implementirane

✅ Avtomatizirani testi pri svakem push/PR  
✅ Multiple Python verzije za backend  
✅ Coverage reporting za oba dela aplikacije  
✅ Artefakti za analizo in arhiviranje  
✅ Clear job structure in step definicije  
✅ PR komentarji s test rezultati  
✅ Test summary za hitro pregled  

## Troubleshooting

### Django Tests Neuspešni
```bash
cd attempt3ip
python manage.py makemigrations
python manage.py migrate
python manage.py test webapp
```

### Jest Tests Neuspešni
```bash
cd attempt3ip
rm -rf node_modules package-lock.json
npm install
npm test
```

### Coverage Issues
- Prepričaj se da je coverage.py ali Jest pravilno instaliran
- Preveri `.gitignore` da ne izključuje test datotek
- Pogledat GitHub Actions logs za podrobnosti
