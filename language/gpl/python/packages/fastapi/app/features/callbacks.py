import time
from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Depends, Query
from fastapi.params import Body
from httpx import AsyncClient
from pydantic import BaseModel, HttpUrl

from app.features.dependency_httpx import get_http_client


router = APIRouter(
    prefix="/callbacks",
    tags=["Callbacks"],
)


class Invoice(BaseModel):
    id: str
    title: str | None = None
    customer: str
    total: float


class InvoiceProcessedEventRequest(BaseModel):
    invoice_id: str
    ok: bool


class InvoiceProcessedEventResponse(BaseModel):
    pass


# ----- Callback API

callback_router = APIRouter()


# This route is not supposed to be exposed in your app!
# It's just an OpenAPI documentation of how your client callback API should look like!
# You can use expressions like {$request.body.id} in your URL
@callback_router.post("{$callback_url}", response_model=InvoiceProcessedEventResponse)
async def invoice_processed_notification(
    body: Annotated[InvoiceProcessedEventRequest, Body()],
):
    pass


# ------ Main API
async def process_invoice(
    invoice: Invoice,
    http_client: AsyncClient,
    callback_url: HttpUrl,
):
    # simulate processing url
    time.sleep(3)

    # tell the client that the invoice has been processed
    response = await http_client.post(
        f"{callback_url}",
        json={
            "invoice_id": invoice.id,
            "ok": True,
        },
    )
    print(response)


@router.post(
    "/invoices/",
    callbacks=callback_router.routes,  # define the callback routes for this API
)
def create_invoice(
    http_client: Annotated[AsyncClient, Depends(get_http_client)],
    background_tasks: BackgroundTasks,
    invoice: Annotated[Invoice, Body()],
    callback_url: Annotated[HttpUrl | None, Query()] = None,
):
    background_tasks.add_task(process_invoice, invoice, http_client, callback_url)
    return {"msg": "Invoice received"}
