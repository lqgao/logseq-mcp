from typing import Dict, List, Optional
from ..client.logseq_client import LogseqAPIClient
from ..mcp import mcp

# Initialize client with configuration
logseq_client = LogseqAPIClient()

@mcp.tool()
def get_all_pages() -> List[Dict]:
    """
    Gets all pages from the Logseq graph.
    
    Journal pages can be identified by the "journal?" attribute set to true and 
    will include a "journalDay" attribute in the format YYYYMMDD.
    
    Returns:
        List of all pages in the Logseq graph.
    """
    return logseq_client.get_all_pages()

@mcp.tool()
def get_page(name: str) -> Optional[Dict]:
    """
    Gets a specific page from the Logseq graph by name.
    
    For journal pages, use the format "mmm dth, yyyy" (e.g., "Apr 4th, 2025").
    Journal pages have specific attributes:
    - "journal?": true - Indicates this is a journal page
    - "journalDay": YYYYMMDD - The date in numeric format
    
    Args:
        name: The name of the page to retrieve.
        
    Returns:
        Information about the requested page, or None if not found.
    """
    return logseq_client.get_page(name)

@mcp.tool()
def create_page(name: str, properties: Optional[Dict] = None) -> Dict:
    """
    Creates a new page in the Logseq graph.
    
    For journal pages, use the format "mmm dth, yyyy" (e.g., "Apr 4th, 2025").
    Logseq automatically sets "journal?": true and "journalDay": YYYYMMDD.
    
    Args:
        name: The name of the new page.
        properties: Optional properties to set on the new page.
        
    Returns:
        Information about the created page.
    """
    return logseq_client.create_page(name, properties)

@mcp.tool()
def delete_page(name: str) -> Dict:
    """
    Deletes a page from the Logseq graph.
    
    ⚠️ This removes the page and all its blocks. Cannot be undone.
    
    Args:
        name: The name of the page to delete.
        
    Returns:
        Result of the deletion operation.
    """
    return logseq_client.delete_page(name)

@mcp.tool()
def get_page_linked_references(page_name: str) -> List[Dict]:
    """
    Gets all linked references to a specific page.
    
    Returns blocks containing [[Page Name]] links to the specified page.
    
    Args:
        page_name: The name of the page to find references to.
        
    Returns:
        List of blocks that reference the specified page.
    """
    return logseq_client.get_page_linked_references(page_name) 