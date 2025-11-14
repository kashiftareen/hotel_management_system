from fastapi import Depends,Response,status,HTTPException,APIRouter
from .. import models,database,schema,hash,basic_auth
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

#to get list of customers from database
@router.get("/",status_code=status.HTTP_200_OK)
def get_list_cus(db:Session=Depends(database.get_db),
                 current_user:models.Customers=Depends(basic_auth.get_current_user)):
    get_cust=db.query(models.Customers).all()
    if get_cust is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return get_cust

# Get a single customer by ID
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_single_cust(id:int,db:Session=Depends(database.get_db),
                    current_user:models.Customers=Depends(basic_auth.get_current_user)):
    get_cust=db.query(models.Customers).filter(models.Customers.id == id).first()
    if get_cust is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"customer with given id {id}  not found"
        )
    return get_cust

# Update a customer by ID
@router.put("/{id}",status_code=status.HTTP_200_OK)
def update_cust(id:int,cust:schema.update_cust,db:Session=Depends(database.get_db),
                current_user:models.Customers=Depends(basic_auth.get_current_user)):
    existing = db.query(models.Customers).filter(models.Customers.id == id).first()
    if existing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"customer with given {id} id not found in this list"
        )
    #update the old database object with new values
    for keys,values in cust.dict(exclude_unset=True).items():
        """it works like this given example
        get.name="ali"
        get.email="kashif@gmail"""
        setattr(existing,keys,values)
    #save changes
    db.commit()
    db.refresh(existing)
    return existing

# Delete a customer by ID
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def update_cust(id:int,db:Session=Depends(database.get_db),
                current_user:models.Customers=Depends(basic_auth.get_current_user)):
    customer = db.query(models.Customers).filter(models.Customers.id == id).first()
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="customer with this id not founded"
        )
    # add and save changes
    db.delete(customer)
    db.commit()
    return {f"customer with the given id {id} successfully deleted"}

