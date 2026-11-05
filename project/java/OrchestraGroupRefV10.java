package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Where a message or block includes a repeating group, by its number, with how many entries it may hold.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraGroupRefV10 extends OrchestraComponentRefV10 {

  private Integer fixrImplMinOccurs;
  private String fixrImplMaxOccurs;


}