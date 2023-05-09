import data
import sender_req

def test_get_order():
    res=sender_req.post_new_order(data.order_body)
    track=res.json()["track"]
    res_order=sender_req.get_order(track)
    assert res_order.status_code==200