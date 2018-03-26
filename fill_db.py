from mainapp.models import ProductCategory, Product, Promo
from json import loads
from os import path


def import_categories(instance):
    items = ProductCategory.objects.all()
    need_add = True
    for item in items:
        if item.name == instance.name:
            need_add = False
    if need_add:
        with ProductCategory(name=instance.name,
                             desciption=instance.description,
                             image=instance.image) as category:
            category.save()


def get_category(name):
    return ProductCategory.objects.filter(name=name)


def import_products(instance):
    items = Product.objects.all()
    need_add = True
    for item in items:
        if item.name == instance.name:
            need_add = False
    if need_add:
        category = get_category(instance.category)
        with Product(name=instance.name,
                     category=category,
                     image=instance.image,
                     short_desc=instance.short_desc,
                     description=instance.description,
                     price=instance.price,
                     quantity=instance.quantity
                     ) as product:
            product.save()


def import_promos(instance):
    items = Promo.objects.all()
    need_add = True
    for item in items:
        if item.name == instance.name:
            need_add = False
    if need_add:
        with Promo(name=instance,
                   desciption=instance.description
                   ) as promo:
            promo.save()


MODEL_CLASSES = {
    "ProductCategory": import_categories,
    "Product": import_products,
    "Promo": import_promos,
}


def get_importer(class_name):
    try:
        return MODEL_CLASSES[class_name]
    except (ValueError, IndexError) as e:
        print(e)
        return None


def import_json(json_data):
    # TODO read json file
    items = []
    importer = None
    try:
        if json_data['modelClass'] is not None:
            importer = get_importer(json_data['modelClass'])
            items = list(json_data['items'])
        for item in items:
            item_obj = loads(item, encoding="utf-8")
            importer(item_obj)
    except ValueError:
        return None


if __name__ == "__main__":
    file_name = "import/promo.json"
    if path.isfile(file_name):
        with open(file_name) as json_file:
            json_data = json_file.read()
            import_json(json_data=json_data)
            json_file.close()
