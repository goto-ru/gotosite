def modeladmin_fields(model, children_fields=None, file_format='csv',
                      fields=None, exclude=None, header=True):
    opts = model._meta
    field_names = set([field.name for field in opts.fields])
    if children_fields:
        for c in children_fields:
            child = getattr(model, c).field.related_model
            child_field_names = set(["%s__%s" % (c, field.name) for field in child._meta.fields])
            field_names |= child_field_names
    if fields:
        fieldset = set(fields)
        field_names = field_names & fieldset
    elif exclude:
        excludeset = set(exclude)
        field_names = field_names - excludeset
    return tuple(field_names)
