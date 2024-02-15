from typing import List
from sqlalchemy.orm import Session

from src.models.models import Contact
from src.models.schemas import ContactModel

async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()

async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name.capitalize(), 
                      last_name=body.last_name.capitalize(), 
                      email=body.email.lower(),
                      phone=body.phone,
                      birthday=body.birthday,
                      notes=body.notes)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name.capitalize()
        contact.last_name = body.last_name.capitalize()
        contact.email = body.email.lower()
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.notes = body.notes
        db.commit()
    db.refresh(contact)
    return contact

async def delete_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

async def find_contacts(first_name: str, last_name: str,
                        email: str, birhdays: int, db: Session) -> List[Contact]:
    if first_name:
        contacts = db.query(Contact).filter(Contact.first_name == first_name.capitalize()).all()
    elif last_name:
        contacts = db.query(Contact).filter(Contact.last_name == last_name.capitalize()).all()
    elif email:
        contacts = db.query(Contact).filter(Contact.email == email.lower()).all()
    # elif birhdays:

    #     contact = db.query(Contact).filter(Contact.birthday < birhdays).all()
    else:
        contacts = None
    return  contacts
    