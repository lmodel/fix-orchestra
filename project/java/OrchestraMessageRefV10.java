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
  A message an action sends, by its number and type code, with the fields it sets or carries over.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraMessageRefV10  {

  private OrchestraIdentifiersV10 fixrIdentifiers;
  private String fixrName;
  private String fixrMsgType;
  private Integer fixrImplMinOccurs;
  private String fixrImplMaxOccurs;
  private int fixrId;
  private String fixrScenario;


}