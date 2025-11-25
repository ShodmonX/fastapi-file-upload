from httpx import AsyncClient
from pathlib import Path


TEST_DIR = Path(__file__).parent / "test_files"

async def test_upload_file(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200

    response = await client.post(
        "/upload/",
        files={"file": open(TEST_DIR / "small.jpg", "rb")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data
    assert "hash" in data
    assert "url" in data
    assert "filename" in data

    response = await client.post(
        "/upload/",
        files={"file": open(TEST_DIR / "small.jpg", "rb")}
    )
    assert response.status_code == 200

    response = await client.post(
        "/upload/",
        files={"file": open(TEST_DIR / "big.jpg", "rb")}
    )
    assert response.status_code == 400

    response = await client.get(
        url = f"/upload/files/{data['hash']}/"
    )
    assert response.status_code == 200

    response = await client.get(
        url=f"/upload/files/invalid_hash/"
    )
    assert response.status_code == 404