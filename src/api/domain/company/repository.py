from api.models.index import db, Company

def get_all_companies():
    companies = Company.query.all()
    companies = list(map(lambda company: company.serialize(), companies))
    return companies
    #checker si es necesario añadir el serialize aquí


def new_company(data):
    new_company = Company(data['name'], data['cif'], data['description'], data['city'], data['adress'],data['phone'], data['email'], data['user_id'])
    db.session.add(new_company)
    db.session.commit()
    return new_company

def delete_company(company_id):
    company = Company.query.get(company_id)
    db.session.delete(company)
    db.session.commit()
    return "Company borrada satisfactoriamente.",201


def update_company(data, company_id,url_logo):
    if not isinstance(data, dict):
        return {'error': 'Formato inválido'}, 400
    company = Company.query.get(company_id)
    if not company:
        return {'error': 'Company not found'}, 404
    company.name = data.get('name')
    company.cif = data.get('cif')
    company.logo = url_logo
    company.adress = data.get('adress')
    company.city = data.get('city')
    company.phone = data.get('phone')
    company.email = data.get ('email')
    company.description = data.get('description')
    db.session.commit()
    return company.serialize(), 200

def get_company(id):
    company = Company.query.get(id)  
    return company



