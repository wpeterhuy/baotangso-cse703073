<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class GuestbookEntry extends Model
{
    protected $table = 'guestbook_entries';
    const UPDATED_AT = null;
    protected $fillable = ['museum_id','user_id','display_name','content','sentiment','is_approved','moderated_at'];
    protected $casts = ['is_approved' => 'boolean', 'moderated_at' => 'datetime'];
    public function museum() { return $this->belongsTo(Museum::class); }
    public function user() { return $this->belongsTo(User::class); }
}
