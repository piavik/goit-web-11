from typing import List
from sqlalchemy.orm import Session

from src.models.models import Contact
from src.models.schemas import ContactModel

def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).query(Contact.id == contact_id).first()

def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name, 
                      last_name=body.last_name, 
                      email=body.email,
                      phone=body.phone,
                      birthday=body.birthday,
                      notes=body.notes)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def update_contact(body: ContactModel, db: Session) -> Contact:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name=body.first_name
        contact.last_name=body.last_name
        contact.email=body.email
        contact.phone=body.phone
        contact.birthday=body.birthday
        contact.notes=body.notes
        db.commit()
    db.refresh(contact)
    return contact

def delete_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

