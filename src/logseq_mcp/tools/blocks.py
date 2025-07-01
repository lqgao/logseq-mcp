from typing import Dict, List, Optional
from ..client.logseq_client import LogseqAPIClient
from ..mcp import mcp

# Initialize client with configuration
logseq_client = LogseqAPIClient()

@mcp.tool()
def get_page_blocks(page_name: str) -> List[Dict]:
    """
    Gets all blocks from a specific page in the Logseq graph.
    
    For journal pages, use the format "mmm dth, yyyy" (e.g., "Apr 4th, 2025").
    Returned blocks contain hierarchical structure information:
      - parent: The parent block's ID
      - level: The indentation level (1 for top-level, 2+ for indented)
      - left: The block to the left (typically the parent for indented blocks)
    
    Args:
        page_name: The name of the page to retrieve blocks from.
        
    Returns:
        List of blocks from the specified page.
    """
    return logseq_client.get_page_blocks(page_name)

@mcp.tool()
def get_block(block_id: str) -> Optional[Dict]:
    """
    Gets a specific block from the Logseq graph by its ID.
    
    The returned block contains hierarchical structure information:
      - parent: The parent block's ID
      - level: The indentation level
      - left: The block to the left
    
    Args:
        block_id: The ID of the block to retrieve.
        
    Returns:
        Information about the requested block, or None if not found.
    """
    return logseq_client.get_block(block_id)

@mcp.tool()
def create_block(page_name: str, content: str, properties: Optional[Dict] = None) -> Dict:
    """
    Creates a new block on a page in the Logseq graph.
    
    Note: Blocks are automatically formatted as bullet points in Logseq UI.
    Use [[Page Name]] to create links to other pages.
    
    Args:
        page_name: The name of the page to create the block on.
        content: The content of the new block.
        properties: Optional properties to set on the new block.
        
    Returns:
        Information about the created block.
    """
    return logseq_client.create_block(page_name, content, properties)

@mcp.tool()
def insert_block(parent_block_id: str, content: str, properties: Optional[Dict] = None, before: bool = False) -> Dict:
    """
    Inserts a new block as a child of the specified parent block.
    
    Creates hierarchical content by adding children to existing blocks.
    The new block is inserted at the beginning (before=True) or end (before=False)
    of the parent's children.
    
    Args:
        parent_block_id: The ID of the parent block to insert under.
        content: The content of the new block.
        properties: Optional properties to set on the new block.
        before: Whether to insert at the beginning of children (default: False).
        
    Returns:
        Information about the created block.
    """
    return logseq_client.insert_block(parent_block_id, content, properties, before)

@mcp.tool()
def update_block(block_id: str, content: str, properties: Optional[Dict] = None) -> Dict:
    """
    Updates an existing block in the Logseq graph.
    
    Use [[Page Name]] to create links to other pages.
    
    Args:
        block_id: The ID of the block to update.
        content: The new content for the block.
        properties: Optional properties to update on the block.
        
    Returns:
        Information about the updated block.
    """
    return logseq_client.update_block(block_id, content, properties)

@mcp.tool()
def move_block(block_id: str, target_block_id: str, as_child: bool = False) -> Dict:
    """
    Moves a block to a new location in the graph.
    
    Moves a block and all its children to a different location.
    - as_child=True: Block becomes a child of the target
    - as_child=False: Block becomes a sibling after the target
    
    Args:
        block_id: The ID of the block to move.
        target_block_id: The ID of the target block to move to.
        as_child: Whether to make the block a child of the target (default: False).
        
    Returns:
        Result of the move operation.
    """
    return logseq_client.move_block(block_id, target_block_id, as_child)

@mcp.tool()
def remove_block(block_id: str) -> Dict:
    """
    Removes a block from the Logseq graph.
    
    ⚠️ Permanently removes the block and all its children. Cannot be undone.
    
    Args:
        block_id: The ID of the block to remove.
        
    Returns:
        Result of the removal operation.
    """
    return logseq_client.remove_block(block_id)

@mcp.tool()
def search_blocks(query: str) -> List[Dict]:
    """
    Searches for blocks matching a query in the Logseq graph.
    
    Query examples:
    - page:"Page Name" - blocks on a specific page
    - "search term" - blocks containing the term
    - [[Page Name]] - references to a specific page
    
    Args:
        query: The search query.
        
    Returns:
        List of blocks matching the search query.
    """
    return logseq_client.search_blocks(query)