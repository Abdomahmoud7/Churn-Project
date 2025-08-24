from pydantic import BaseModel, Field
from typing import Literal

class CustomerData(BaseModel):
    CreditScore: int = Field(description="Credit score of the customer")
    Geography: Literal["France", "Spain", "Germany"] = Field(description="customer's country")
    Gender: Literal["Male", "Female"] = Field(description="customer's gender")
    Age: int = Field(description="customer's age", ge=18, le=100)
    Tenure: int = Field(description="Years as a customer (0-10)", ge=0, le=10)
    Balance: float = Field(description="customer's account balance", ge=0)
    NumOfProducts: int = Field(description="Number of bank products the customer is using (1-4)", ge=1, le=4)
    HasCrCard: Literal[0, 1] = Field(description="Does the customer have a credit card? (1=Yes, 0=No)")
    IsActiveMember: Literal[0, 1] = Field(description="Active member status (1=Yes, 0=No)")
    EstimatedSalary: float = Field(description="Estimated annual salary", ge=0)

