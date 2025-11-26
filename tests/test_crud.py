from app.crud import get_file, create_file, update_file_status, update_file_thumbnail


async def test_create_and_get_file(test_db, client):
    file_obj = await create_file(
        db=test_db,
        hash="abc123",
        filename="test.jpg",
        path="/uploads/test.jpg",
        user_id=999
    )
    assert file_obj
    assert 'hash' in file_obj
    assert file_obj['hash'] == "abc123"
    assert 'processed' in file_obj
    assert file_obj['processed'] is False

    fetched = await get_file(test_db, "abc123")
    assert fetched
    assert 'id' in fetched
    assert fetched['id'] == file_obj['id']

async def test_update_status_and_thumbnail(test_db, client):
    file_obj = await create_file(test_db, "def456", "a.png", "/tmp/a.png", 1)

    assert file_obj
    await update_file_status(test_db, file_obj['id'], "success", processed=True)
    await update_file_thumbnail(test_db, file_obj['id'], "/uploads/thumbs/thumb_a.png")

    file_obj = await get_file(test_db, "def456")
    assert file_obj
    assert file_obj['processing_status'] == "success"
    assert file_obj['processed'] is True
    assert file_obj['thumbnail_path'] == "/uploads/thumbs/thumb_a.png"