import axios from "axios";

const PARTNER_TYPE_RESOURCE = "/partner-type/";
const PARTNER_RESOURCE = "/partner/";
const PRODUCT_CATEGORY_RESOURCE = "/product-category/";
const PURCHASE_OPPORTUNITY_RESOURCE = "/purchase-opportunity/";

export const client = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 1000,
});

// Product
export const ProductCategoryService = {
  getAll() {
    return client.get(`${PRODUCT_CATEGORY_RESOURCE}`).catch((error) => {
      throw new Error(`ProductCategoryService ${error}`);
    });
  },

  byId(id) {
    return client.get(`${PRODUCT_CATEGORY_RESOURCE}/${id}`).catch((error) => {
      throw new Error(`ProductCategoryService ${error}`);
    });
  },
};

// Partner
export const PartnerService = {
  getAll() {
    return client.get(`${PARTNER_RESOURCE}`).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },

  byId(id) {
    return client.get(`${PARTNER_RESOURCE}/${id}`).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },

  allByPartnerType(partnerTypeId) {
    return client
      .get(`${PARTNER_RESOURCE}partner-type/${partnerTypeId}`)
      .catch((error) => {
        throw new Error(`PartnerService ${error}`);
      });
  },

  create(partner) {
    return client.post(`${PARTNER_RESOURCE}`, partner).catch((error) => {
      throw new Error(`PartnerService ${error}`);
    });
  },
};

// Partner Types
export const PartnerTypeService = {
  getAll() {
    return client.get(`${PARTNER_TYPE_RESOURCE}`).catch((error) => {
      throw new Error(`PartnerTypeService ${error}`);
    });
  },

  byId(id) {
    return client.get(`${PARTNER_TYPE_RESOURCE}/${id}`).catch((error) => {
      throw new Error(`PartnerTypeService ${error}`);
    });
  },
};

// Purchase Opportunity
export const PurchaseOpportunityService = {
  getAll(params) {
    if (params) {
      return client
        .get(`${PURCHASE_OPPORTUNITY_RESOURCE}`, { params })
        .catch((error) => {
          throw new Error(`PurchaseOpportunityService ${error}`);
        });
    }
    return client.get(`${PURCHASE_OPPORTUNITY_RESOURCE}`).catch((error) => {
      throw new Error(`PurchaseOpportunityService ${error}`);
    });
  },

  byId(id) {
    return client
      .get(`${PURCHASE_OPPORTUNITY_RESOURCE}${id}`)
      .catch((error) => {
        throw new Error(`PurchaseOpportunityService ${error}`);
      });
  },

  getAllStatus() {
    return client
      .get(`${PURCHASE_OPPORTUNITY_RESOURCE}status/all`)
      .catch((error) => {
        throw new Error(`PurchaseOpportunityService ${error}`);
      });
  },
};
