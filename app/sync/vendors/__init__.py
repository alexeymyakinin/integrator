from app.sync.vendors import amazon

vendors = {
    'amazon': amazon.get_adapter()
}

__all__ = ['vendors']
